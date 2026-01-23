# 更新日志 (Changelog)

所有重要的项目更新都将记录在此文件中。

## [Unreleased]

### ✨ 新增特性 (Features)

- **文档智能重构 (Document Intelligent Refactoring)**:
  - 新增 `refactor_smb.py`: 针对 SMB100A 手册的规则引擎重构脚本，实现了目录移除、标题层级自动修复、警告信息格式标准化及图片占位符处理。
  - 新增 `fix_tables_ai.py`: 基于 DeepSeek API (LLM) 的表格智能修复工具，可自动识别并修复 Markdown 表格中的断行、合并单元格及错位问题。
  - 生成了 `docs/visual_optimized/` 目录下的重构版本手册：
    - `SMB100A_OperatingManual_cn_sample.md`: 规则优化后的中间版本。
    - `SMB100A_OperatingManual_cn_ai_tables.md`: 经过 AI 表格修复的最终优化版本。

- **网络鲁棒性 (Network Robustness)**:
  - `DeepSeekClient` 新增指数退避重试机制 (Exponential Backoff)。
  - 支持自动识别可重试的网络错误 (timeout, connection reset, 502/503/504)。
  - 最多重试 5 次，每次等待时间指数增长 (2s -> 4s -> 8s... 最大 60s)。

### ♻️ 结构重构 (Refactor)

- **工程化重构 (Project Restructuring)**:
  - 实施了符合高级工程标准的目录结构：`docling_core`, `ai_adapter`, `database`。
  - 将翻译模块迁移至 `ai_adapter/translation_agent`。
  - 建立了严格的 `rules/` 和 `.cursorrules` 全局规范。
  - **Git Workflow**: 引入 Translation 独立分支策略。

### ✨ 新增特性 (Features)

- **DeepSeek 翻译流水线 (Translation Pipeline)**:
  - 实现了基于 KV Cache 和 JSON Mode 的稳健翻译 Agent。
  - 增加了 SCPI 指令保护 (`SCPIGuard`)。

- **生产环境部署 (Production Deployment)**:
  - 将 AI 优化后的 SMB100A 中文手册 (`SMB100A_OperatingManual_cn_ai_tables.md`) 正式部署至 `database/production/i18n/zh-cn/v1.0_20260123/`，替换了旧版文件。
  - 该版本修复了 95% 以上的表格排版问题，并应用了最新的视觉优化规则。

### ♻️ 结构重构 (Refactor)

- **文档体系重组 (Documentation Restructuring)**:
  - **资产迁移**: 将 `visual_optimized` 移至 `database/`，确立核心数据资产地位。
  - **文档归类**:
    - `docs/guides/`: 存放技术规范与指南 (Tmux, Git, API 等)。
    - `docs/planning/`: 存放开发计划与创意草稿。
    - `docs/archive/`: 归档旧版测试文件。
  - **规范化**: 强制所有文档文件名采用全英文 (ASCII) 命名，移除非 ASCII 字符。

## [0.2.0] - 2026-01-22

### ✨ 新增特性 (Features)

- **文档结构化生成器 (`generate_structured_md.py`)**:
  - 新增了从 Docling JSON 直接生成高质量 Markdown 的工具。
  - 支持 **页码注入**：在 Markdown 中自动插入 `<!-- Page X -->` 注释，实现原文精准溯源。
  - 支持 **不规则表格清洗**：针对 OE1022D 手册中 `SENSD` 等命令表存在的“命令列重复”问题，实现了垂直去重逻辑，大幅提升了相关表格的可读性和机器解析能力。

- **OE1022D 转化流程 (OE1022D Pipeline)**:
  - 完成了 OE1022D 锁相放大器手册的 **原型迭代转化** (Pages 62-82)。
  - 验证了自定义 Markdown 生成器在处理复杂命令列表时的有效性。

### ♻️ 结构重构 (Refactor)

- **知识库目录重组 (`knowledge_base/`)**:
  - 建立了清晰的 **生产环境 (Production)** 与 **归档环境 (Archive)** 分离机制。
  - `production/`: 存放经过清洗、验证、可直接供 AI 调用的最终版知识库 (SMB100A, RsInstrument)。
  - `archive/`: 存放所有中间实验数据、原始运行记录 (OE1022D Runs)。
  - 更新了 `knowledge_base/README.md` 以反映新的目录规范。

### 🐛 问题修复 (Bug Fixes)

- 修复了 Docling 转换中多行合并单元格识别错误导致的命令冗余问题。
- 优化了长文本描述被错误识别为表格表头的问题。

## [0.1.0] - 2026-01-20

### 🎉 初始发布

- 初始化 Docling PDF 转换流水线。
- 完成 SMB100A 信号发生器手册的全量转换与知识库构建。
- 集成 NVIDIA GPU 加速支持 (RapidOCR, TableFormer)。
