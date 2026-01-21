---
description: Finish a feature branch and merge into dev
---

1. Ensure all changes are committed (check `git status`).
2. Switch to `dev` branch:
   ```bash
   git checkout dev
   git pull origin dev
   ```
3. Merge the feature branch:
   ```bash
   git merge --no-ff <feature_branch_name>
   ```
4. Push `dev` to remote:
   ```bash
   git push origin dev
   ```
5. Delete the local feature branch:
   ```bash
   git branch -d <feature_branch_name>
   ```
6. Notify the user the feature is merged.
