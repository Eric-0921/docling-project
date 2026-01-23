# Git Workflow Standards [STRICT]

> 本规则定义了 docling-project 的分支管理和提交规范，必须严格遵守。

## 1. Branch Strategy (分支策略)

- **`main`**: 生产环境稳定分支。**严禁直接 Push**，仅接受来自 `dev` 的 Merge。
- **`dev`**: 主开发分支。所有 Feature 分支必须由此切出，并最终合并回此。
- **`feat/<name>`**: 功能开发分支 (e.g., `feat/pdf-parser-v2`)。
- **`fix/<name>`**: Bug 修复分支 (e.g., `fix/memory-leak`)。
- **`docs/<name>`**: 文档/知识库更新。

## 2. Commit Message Convention (提交规范)

必须遵循 **Conventional Commits**: `<type>(<scope>): <subject>`

### Types

- **feat**: 新功能 (New Feature)
- **fix**: 修复 Bug
- **docs**: 文档/知识库变更
- **style**: 格式化 (不影响代码运行)
- **refactor**: 代码重构 (无新功能/Bug修复)
- **chore**: 构建系统/依赖更新 (e.g., `backup`, `config`)

### Example

- ✅ `feat(parser): add table extraction support for smb100a`
- ❌ `update code`

## 3. Workflow Protocol

1. **Start**: `git checkout dev` -> `git pull` -> `git checkout -b feat/xxx`
2. **Work**: Develop code -> Verify -> Backup if critical.
3. **Commit**: `git add .` -> `git commit -m "..."`
4. **Finish**: Switch to `dev` -> `git merge --no-ff feat/xxx` -> `git push`
