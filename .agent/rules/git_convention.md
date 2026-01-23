---
description: Git workflow and commit message conventions
---

# Git Workflow & Conventions

## 1. Branch Strategy

- **`main`**: Stable production branch. Only accepts merges from `dev`.
- **`dev`**: Main development branch.
- **`feat/<name>`**: Feature development (checkout from `dev`).
- **`docs/<name>`**: Documentation updates.
- **`feature/translation-system-v1`**: Specific long-lived feature branch for translation system.

## 2. Commit Message Convention

Follow **Conventional Commits**: `<type>(<scope>): <subject>`

### Types

- **feat**: New feature (e.g., `feat(lockin): add basic connect script`)
- **fix**: Bug fix (e.g., `fix(parser): resolve pdf table extraction error`)
- **docs**: Documentation/KB changes (e.g., `docs(kb): update smb100a command list`)
- **style**: Formatting changes (no logic change)
- **refactor**: Code refactoring (e.g., `refactor(core): cleanup deepseek client`)
- **chore**: Build/Tools/Maintenance

### Rules

- Subject must be in English (preferred) or Chinese (allowed if clear).
- Keep subject concise (under 50 chars ideally).

## 3. Workflow

1. Checkout `dev` (or feature branch).
2. Create/Switch to `feat/xxx`.
3. Develop & Test.
4. Commit using conventions.
5. Push & PR.
