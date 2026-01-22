# 更新日志 (Changelog)

所有重要的项目更新都将记录在此文件中。

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
