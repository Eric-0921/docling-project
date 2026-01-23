# Git Workflow Standards

1.  **Commit Messages**:
    -   Format: `<type>: <description>` (in Chinese)
    -   Types:
        -   `feat`: 新功能 (New Feature)
        -   `fix`: 修复 Bug (Bug Fix)
        -   `docs`: 文档变更 (Documentation)
        -   `refactor`: 代码重构 (Refactor)
        -   `chore`: 杂务/构建/工具 (Chores)
    -   Example: `feat: 实现 DeepSeek 翻译客户端`

2.  **Branching**:
    -   `main` / `dev`: Protected branches.
    -   `feature/*`: Feature development.
    -   `hotfix/*`: Urgent fixes.

3.  **Changelog**:
    -   Update `CHANGELOG.md` before merging to `main`/`dev`.
