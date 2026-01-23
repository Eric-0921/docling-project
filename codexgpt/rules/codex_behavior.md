# CodexGPT 行为规则（项目约束）

以下规则用于在 Codex 中模拟 Antigravity 的工作方式，并确保不影响现有项目内容。

## 必须遵守

1. 仅在 `doclingprj1` Conda 环境内执行命令。  
   - 所有终端命令需显式 `conda activate doclingprj1`。

2. 所有操作必须在终端内可见。  
   - 任何读取、写入、查询等动作都要通过命令执行并展示输出。

3. 不得删除或修改既有内容，只允许新增并标注。  
   - 禁止删除或改写：`knowledge_base/`、`docling_pipeline/`、`instrument_control/`、`docs/`、`.agent/` 及其子目录的原有内容。
   - 允许新增：以上目录及 `codexgpt/` 内可新增文件，但文件名与文件内容必须标注 `codex` 生成来源。

## 交互约定

1. 每新增一个文件，必须先说明意图并等待用户审查通过再写入。  
2. 如需更大范围操作（测试、安装依赖等），必须先征得用户确认。  
3. 如需提交版本更新，提交信息与 `CHANGELOG.md` 必须标注为 Codex 完成。  
