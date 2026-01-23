# CodexGPT 迁移区（仅 Codex 使用）

本目录用于把 Antigravity 里的自定义 skills/workflows 迁移为 Codex 可读的提示模板与规则文件。
所有改动严格限制在 `codexgpt/` 内，不修改原项目的知识库、脚本或已有配置。

## 使用方式（简要）

1. 打开索引：`codexgpt/index.md`
2. 先加载规则：`codexgpt/rules/codex_behavior.md`
3. 按需加载技能提示：`codexgpt/skills/<skill>/prompt.md`
4. 按需参考流程：`codexgpt/workflows/<flow>.md`

## 目录结构

- `codexgpt/index.md`：入口索引
- `codexgpt/rules/`：Codex 行为与约束
- `codexgpt/skills/`：迁移后的技能提示模板
- `codexgpt/workflows/`：迁移后的流程说明
- `codexgpt/agent_migration_cn.md`：Antigravity 与 Codex 的差异与自定义说明（中文）
