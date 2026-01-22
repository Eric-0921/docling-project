# Docling PDF Conversion Project for R&S Instruments

本项目实现了一个高性能、基于 GPU 加速的 PDF 转换流水线，旨在将复杂的罗德与施瓦茨 (R&S) 仪器技术手册转化为 AI 友好的结构化知识库 (Markdown/JSON)。项目利用最新的 **Docling** 技术栈（结合 NVIDIA GPU 加速和 Hugging Face 模型）来处理复杂的表格、SCPI 命令和技术公式。

## 🚀 核心特性 (Features)

- **GPU 深度加速**: 基于 NVIDIA A4000 优化，使用 `RapidOCR` (Torch 后端) 实现毫秒级 OCR 推理。
- **高精度版面分析**: 集成 `DocLayNet` 模型，精准识别多栏排版、侧边栏注释及复杂图文混排。
- **智能表格还原**: 采用 `TableFormer` (ACCURATE 模式) 完美重建 SCPI 命令参数表，支持 **合并单元格识别** 和 **垂直去重**。
- **页码级溯源**: 生成的 Markdown 包含 `<!-- Page X -->` 锚点，可直接从知识库定位回 PDF 原文页码。
- **SCPI 语义增强**: 针对仪器控制领域优化，确保 `:SOURce:FREQuency:CW` 等关键指令格式不被破坏。

## 📂 项目结构 (Structure)

项目采用 **Monorepo** 结构，分离了转换流水线代码与生成的知识库数据。

```
docling-project/
├── docling_pipeline/        # 核心转换代码
│   ├── scripts/             # 执行脚本
│   │   ├── convert_pdf.py   # PDF -> JSON/MD 转换主程序
│   │   ├── run_oe1022d.sh   # 自动化运行脚本
│   │   └── generate_structured_md.py # [NEW] 结构化 Markdown 生成器
│   └── config/              # 设备专属配置 (SMB100A, OE1022D)
│
├── knowledge_base/          # 知识库数据存储
│   ├── production/          # ✅ 生产环境：清洗完成的最终知识库
│   │   ├── smb100a/         # SMB100A 信号发生器
│   │   └── rsinstrument/    # RsInstrument Python 库
│   └── archive/             # 🗄️ 归档环境：实验数据与中间产物
│       ├── oe1022d_runs/    # OE1022D 转换实验记录
│       └── ...
│
└── .agent/                  # AI Agent 技能与工作流定义
```

## 🛠️ 环境安装 (Setup)

### 前置要求
- **操作系统**: Linux (Ubuntu 22.04 推荐)
- **显卡**: NVIDIA GPU (支持 CUDA 13.0+, 推荐 16GB+ 显存)
- **环境管理**: Conda / Mamba

### 安装步骤

1. **创建 Conda 环境**
   ```bash
   conda create -n doclingprj1 python=3.10
   conda activate doclingprj1
   ```

2. **安装 PyTorch (CUDA 13.0)**
   > ⚠️ 关键：必须与系统 CUDA 版本匹配
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
   ```

3. **安装 Docling 全套件**
   ```bash
   pip install "docling[easyocr,rapidocr,vlm]"
   ```

4. **下载预训练模型**
   ```bash
   docling-tools models download
   ```

## ⚡ 使用指南 (Usage)

### 1. 运行标准转换
使用 `convert_pdf.py` 将 PDF 转换为基础 Markdown 和 JSON 数据：

```bash
# 示例：转换 OE1022D 手册的第 62-82 页
python docling_pipeline/scripts/convert_pdf.py \
    --input oe1022d-lockin.pdf \
    --output knowledge_base/archive/oe1022d_runs \
    --pages "62-82"
```

### 2. 生成结构化增强文档 (推荐)
使用我们定制的生成器，从 JSON 产出带有页码和清洗表格的 Markdown：

```bash
# 读取 JSON 输出，生成优化后的 Markdown
python docling_pipeline/scripts/generate_structured_md.py \
    knowledge_base/archive/oe1022d_runs/run_latest/raw/oe1022d-lockin.json
```

### 3. 查看知识库
生成的知识库文件位于 `knowledge_base/` 目录。
- **Production**: 可直接用于 RAG 检索或 Agent 上下文。
- **Archive**: 包含了转换过程中的原始数据，用于调试解析问题。

## 🧩 模型配置表

| 能力 | 模型 / 引擎 | 配置参数 |
|------|------------|----------|
| **版面分析** | `DocLayNet` | `page_batch_size=16` |
| **表格识别** | `TableFormer` | `TableFormerMode.ACCURATE` |
| **OCR 引擎** | `RapidOCR` | `backend="torch"` (GPU) |
| **公式增强** | `CodeFormula` | `do_code_enrichment=True` |

## 🔗 参考资料

- **Official GitHub**: [DS4SD/docling](https://github.com/DS4SD/docling)
- **Hugging Face Org**: [docling-project](https://huggingface.co/docling-project)
