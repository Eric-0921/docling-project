---
description: Start a new feature/task safely
---

1. Ensure workspace is clean.

   ```bash
   git status --porcelain
   ```

2. Update `dev` reference properly.

   ```bash
   git checkout dev || git checkout -b dev origin/dev
   git pull origin dev
   ```

3. Propose a branch name (format: `feat/xxx` or `fix/xxx`).

// turbo 4. Create and switch to new branch.

```bash
git checkout -b <branch_name>
```

5. Ready to work.
