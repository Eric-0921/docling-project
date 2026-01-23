# Docling Pipeline (文档解析流水线)

本模块负责将非结构化的技术文档（PDF, Web Pages）转换为结构化的知识库。

## 核心功能

### 1. PDF 智能转换 (`docling_core`)

利用 IBM Docling 技术栈处理复杂 PDF。

- **布局分析**: 自动识别 Headers, Paragraphs, Images。
- **高精度表格**: 使用 `TableFormer` 还原跨页、合并单元格的表格。
- **公式识别**: 自动提取 LaTeX 格式公式。

### 2. 多源数据摄取

不仅仅是 PDF，还支持网络文档爬取。

- **`scrape_rsinstrument.py`**: 专门用于爬取 `RsInstrument` 官方 Python 文档，补充 API 编程知识。

### 目录结构

- `input/`: 放置待转换的原始 PDF。
- `strategies/`: 针对不同厂商（R&S, OE）的特定解析策略模式（Strategy Pattern）。
- `scripts/`: 辅助工具脚本。

## 使用指南

```bash
# 转换特定 PDF (指定页码范围)
python convert_pdf.py --input input/device_manual.pdf --page-range 62-82

# 结果将输出到 prototype_output/ 目录
```
