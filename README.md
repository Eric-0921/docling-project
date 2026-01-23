# Intelligent Instrument Control Project (Docling + AI)

> **Project Status**: Active Development (Main Branch)
> **Core Focus**: SCPI Instrument Control via AI Knowledge Base

这是一个集成 **Docling PDF 解析**、**AI 知识库构建** 和 **自动化仪器控制** 的综合工程。项目旨在利用最新的 DeepSeek 模型和 Docling 解析技术，将原本晦涩的硬件手册转化为机器可理解的结构化数据，并配合 Agent 实现自动化测试。

## 📂 Project Structure (核心架构)

### 1. [docling_pipeline/](./docling_pipeline/)

**PDF Conversion & Knowledge Extraction Core**

- 负责将原始 PDF 手册 (SMB100A, OE1022D) 转换为 Markdown/JSON。
- 集成了 `TableFormer` 和 `DocLayNet`，专门优化技术手册的表格和公式解析。
- 包含 `scrape_rsinstrument.py` 用于爬取在线 Python 库文档。

### 2. [instrument_control/](./instrument_control/)

**Hardware Interaction Layer**

- 存放实际控制仪器的 Python 脚本。
- `drivers/`: 封装 PyVISA 和 Socket 通信的基础驱动。
- `experiments/`: 具体实验流程（如频率扫描、Lock-in 测量）。

### 3. [ai_adapter/](./ai_adapter/)

**LLM Integration Interface**

- AI 翻译与指令生成模块。
- 负责连接 DeepSeek/OpenAI API，实现自然语言到 SCPI 指令的转译。

### 4. [.agent/](./.agent/)

**Agentic Workflow Configuration**

- 包含 `rules`, `skills`, `workflows`。
- 定义了 AI 助手的行为规范（如强制中文回复、Git 提交流程）。

---

## 🚀 Quick Start

### Environment Setup

```bash
# 激活 Conda 环境
conda activate doclingprj1

# 安装依赖
pip install -r requirements.txt
```

### Key Scripts

- **Run PDF Conversion**:
  ```bash
  python docling_pipeline/convert_pdf.py --input manuals/smb100a.pdf
  ```
- **Run Instrument Demo**:
  ```bash
  python instrument_control/experiments/freq_sweep_demo.py
  ```

## 📜 Development Standards

- **Language**: 所有文档和注释强制使用 **中文**。
- **Git Flow**: 使用 `feature/name` 分支开发，通过 PR 合并至 `main`。
- **Commit**: 遵循 Conventional Commits (`feat:`, `fix:`, `chore:`).

---

_Maintained by Eric-0921 & Antigravity Agent_
