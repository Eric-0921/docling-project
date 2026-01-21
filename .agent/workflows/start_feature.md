---
description: Start a new feature or task using standard git flow
---

1. Check current status with `git status`.
2. Ensure we are on `dev` branch:
   ```bash
   git checkout dev
   git pull origin dev
   ```
   (If `dev` does not exist, create it from `main`: `git checkout -b dev`)
3. Propose a branch name based on the task description. Format: `feat/short-description` or `docs/short-description` or `fix/short-description`.
4. Create and switch to the new branch:
   ```bash
   git checkout -b <branch_name>
   ```
5. Inform the user that the workspace is ready for the new task.
