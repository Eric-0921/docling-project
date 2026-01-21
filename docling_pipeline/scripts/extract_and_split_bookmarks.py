#!/usr/bin/env python3
"""
PDF 书签提取与拆分工具
根据 PDF 书签（大纲）将文档拆分为多个独立的 PDF 文件。

功能：
- 递归读取所有层级的书签
- 按书签范围拆分 PDF
- 使用"数字标号_书签标题"命名
- 生成 bookmarks.json 元数据索引
- 详细的日志记录和进度条显示
"""

import os
import re
import json
import argparse
import logging
import time
from pathlib import Path
from datetime import datetime

# Rich 进度条和控制台
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.table import Table
from rich.panel import Panel
from rich import box

# PDF 处理
from PyPDF2 import PdfReader, PdfWriter


# 设置日志
def setup_logging(output_dir: Path):
    """配置日志记录器"""
    log_file = output_dir / "split_bookmarks.log"
    
    # 创建 formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # 获取 logger
    logger = logging.getLogger('bookmark_splitter')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    
    return logger


def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符"""
    # 替换非法字符
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    # 替换多个空格为单个下划线
    name = re.sub(r'\s+', ' ', name).strip()
    # 限制长度
    if len(name) > 100:
        name = name[:100]
    return name


def get_page_number(dest, reader):
    """从书签目标获取页码"""
    try:
        if hasattr(dest, 'page'):
            # 获取页面对象
            page = dest.page
            if page is not None:
                # 查找页面索引
                for i, p in enumerate(reader.pages):
                    if p.indirect_reference == page:
                        return i
        return None
    except Exception:
        return None


def extract_bookmarks_recursive(outline, reader, parent_number="", level=0):
    """
    递归提取书签信息
    
    返回格式：
    [
        {
            "number": "1",
            "title": "Getting Started",
            "level": 0,
            "page": 10,
            "children": [...]
        },
        ...
    ]
    """
    bookmarks = []
    counter = 1
    
    for item in outline:
        if isinstance(item, list):
            # 这是一个子列表（嵌套书签）
            if bookmarks:
                # 将子书签添加到上一个书签的 children 中
                parent = bookmarks[-1]
                parent_num = parent["number"]
                children = extract_bookmarks_recursive(item, reader, parent_num, level + 1)
                parent["children"] = children
        else:
            # 这是一个书签对象
            current_number = f"{parent_number}.{counter}" if parent_number else str(counter)
            
            # 获取页码
            page_num = None
            try:
                if hasattr(item, 'page'):
                    page = item.page
                    if page is not None:
                        for i, p in enumerate(reader.pages):
                            if p.indirect_reference == page:
                                page_num = i
                                break
            except Exception:
                pass
            
            bookmark = {
                "number": current_number,
                "title": item.title if hasattr(item, 'title') else str(item),
                "level": level,
                "page": page_num,
                "children": []
            }
            bookmarks.append(bookmark)
            counter += 1
    
    return bookmarks


def flatten_bookmarks(bookmarks, result=None):
    """将嵌套的书签结构展平为列表"""
    if result is None:
        result = []
    
    for bm in bookmarks:
        result.append({
            "number": bm["number"],
            "title": bm["title"],
            "level": bm["level"],
            "page": bm["page"]
        })
        if bm.get("children"):
            flatten_bookmarks(bm["children"], result)
    
    return result


def calculate_page_ranges(flat_bookmarks, total_pages):
    """计算每个书签的页码范围（起始页到结束页）"""
    # 按页码排序
    sorted_bookmarks = sorted(
        [b for b in flat_bookmarks if b["page"] is not None],
        key=lambda x: x["page"]
    )
    
    ranges = []
    for i, bm in enumerate(sorted_bookmarks):
        start_page = bm["page"]
        
        # 结束页为下一个书签的起始页 - 1，或者最后一页
        if i + 1 < len(sorted_bookmarks):
            end_page = sorted_bookmarks[i + 1]["page"] - 1
        else:
            end_page = total_pages - 1
        
        # 确保结束页不小于起始页
        if end_page < start_page:
            end_page = start_page
        
        ranges.append({
            "number": bm["number"],
            "title": bm["title"],
            "level": bm["level"],
            "start_page": start_page,
            "end_page": end_page,
            "page_count": end_page - start_page + 1
        })
    
    return ranges


def split_pdf_by_bookmarks(input_path: Path, output_dir: Path, console: Console, logger: logging.Logger):
    """主函数：按书签拆分 PDF"""
    
    start_time = time.time()
    
    # 任务开始信息
    console.print(Panel.fit(
        f"[bold cyan]PDF 书签拆分工具[/bold cyan]\n"
        f"输入文件：{input_path.name}\n"
        f"输出目录：{output_dir}",
        title="任务信息",
        border_style="cyan"
    ))
    
    logger.info("=" * 60)
    logger.info("PDF 书签拆分任务开始")
    logger.info(f"输入文件：{input_path}")
    logger.info(f"输出目录：{output_dir}")
    
    # 读取 PDF
    console.print("\n[bold]正在读取 PDF 文件...[/bold]")
    try:
        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)
        console.print(f"  ✓ 成功读取，共 {total_pages} 页")
        logger.info(f"PDF 读取成功，共 {total_pages} 页")
    except Exception as e:
        console.print(f"[bold red]  ✗ 读取 PDF 失败：{e}[/bold red]")
        logger.error(f"读取 PDF 失败：{e}")
        return
    
    # 提取书签
    console.print("\n[bold]正在提取书签...[/bold]")
    try:
        outline = reader.outline
        if not outline:
            console.print("[bold red]  ✗ PDF 中没有书签！[/bold red]")
            logger.error("PDF 中没有书签")
            return
        
        bookmarks = extract_bookmarks_recursive(outline, reader)
        flat_bookmarks = flatten_bookmarks(bookmarks)
        console.print(f"  ✓ 找到 {len(flat_bookmarks)} 个书签")
        logger.info(f"提取到 {len(flat_bookmarks)} 个书签")
    except Exception as e:
        console.print(f"[bold red]  ✗ 提取书签失败：{e}[/bold red]")
        logger.error(f"提取书签失败：{e}")
        return
    
    # 计算页码范围
    page_ranges = calculate_page_ranges(flat_bookmarks, total_pages)
    
    # 显示书签预览表格
    preview_table = Table(title="书签预览（前10个）", box=box.SIMPLE)
    preview_table.add_column("编号", style="cyan")
    preview_table.add_column("标题", style="white")
    preview_table.add_column("页码范围", style="green")
    
    for bm in page_ranges[:10]:
        indent = "  " * bm["level"]
        preview_table.add_row(
            bm["number"],
            f"{indent}{bm['title'][:40]}{'...' if len(bm['title']) > 40 else ''}",
            f"{bm['start_page']+1}-{bm['end_page']+1} ({bm['page_count']}页)"
        )
    
    if len(page_ranges) > 10:
        preview_table.add_row("...", f"... 还有 {len(page_ranges) - 10} 个书签 ...", "...")
    
    console.print(preview_table)
    
    # 开始拆分
    console.print(f"\n[bold]开始拆分 PDF（共 {len(page_ranges)} 个文件）...[/bold]\n")
    logger.info(f"开始拆分，共 {len(page_ranges)} 个书签")
    
    success_count = 0
    error_count = 0
    results = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        task = progress.add_task("拆分中...", total=len(page_ranges))
        
        for bm in page_ranges:
            # 生成文件名
            filename = f"{bm['number']}_{sanitize_filename(bm['title'])}.pdf"
            output_path = output_dir / filename
            
            progress.update(task, description=f"正在处理：{bm['number']} {bm['title'][:30]}...")
            
            try:
                # 创建新的 PDF
                writer = PdfWriter()
                for page_num in range(bm["start_page"], bm["end_page"] + 1):
                    writer.add_page(reader.pages[page_num])
                
                # 写入文件
                with open(output_path, "wb") as f:
                    writer.write(f)
                
                success_count += 1
                results.append({
                    "number": bm["number"],
                    "title": bm["title"],
                    "filename": filename,
                    "start_page": bm["start_page"] + 1,  # 转为 1-indexed
                    "end_page": bm["end_page"] + 1,
                    "page_count": bm["page_count"],
                    "status": "success"
                })
                logger.info(f"成功：{filename} (页码 {bm['start_page']+1}-{bm['end_page']+1})")
                
            except Exception as e:
                error_count += 1
                results.append({
                    "number": bm["number"],
                    "title": bm["title"],
                    "filename": filename,
                    "status": "error",
                    "error": str(e)
                })
                logger.error(f"失败：{filename} - {e}")
            
            progress.advance(task)
    
    # 保存元数据
    metadata = {
        "source_file": input_path.name,
        "total_pages": total_pages,
        "total_bookmarks": len(page_ranges),
        "success_count": success_count,
        "error_count": error_count,
        "created_at": datetime.now().isoformat(),
        "bookmark_tree": bookmarks,
        "files": results
    }
    
    metadata_path = output_dir / "bookmarks.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    logger.info(f"元数据已保存到：{metadata_path}")
    
    # 完成统计
    elapsed_time = time.time() - start_time
    
    summary_table = Table(title="任务完成", box=box.ROUNDED)
    summary_table.add_column("项目", style="cyan")
    summary_table.add_column("数值", style="bold")
    summary_table.add_row("总书签数", str(len(page_ranges)))
    summary_table.add_row("成功拆分", f"[green]{success_count}[/green]")
    summary_table.add_row("失败", f"[red]{error_count}[/red]" if error_count > 0 else "0")
    summary_table.add_row("总耗时", f"{elapsed_time:.2f} 秒")
    summary_table.add_row("元数据文件", "bookmarks.json")
    summary_table.add_row("日志文件", "split_bookmarks.log")
    
    console.print("\n")
    console.print(summary_table)
    
    logger.info("=" * 60)
    logger.info(f"任务完成：成功 {success_count}，失败 {error_count}，耗时 {elapsed_time:.2f} 秒")
    logger.info("=" * 60)
    
    if error_count > 0:
        console.print(f"\n[yellow]注意：有 {error_count} 个书签拆分失败，请查看日志文件了解详情。[/yellow]")


def main():
    parser = argparse.ArgumentParser(
        description="PDF 书签提取与拆分工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python extract_and_split_bookmarks.py --input manual.pdf --output output_split/
        """
    )
    parser.add_argument("--input", "-i", type=str, required=True, help="输入 PDF 文件路径")
    parser.add_argument("--output", "-o", type=str, default="output_split", help="输出目录（默认：output_split）")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output)
    
    # 创建控制台
    console = Console()
    
    # 检查输入文件
    if not input_path.exists():
        console.print(f"[bold red]错误：输入文件不存在：{input_path}[/bold red]")
        return 1
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 设置日志
    logger = setup_logging(output_dir)
    
    # 执行拆分
    split_pdf_by_bookmarks(input_path, output_dir, console, logger)
    
    return 0


if __name__ == "__main__":
    exit(main())
