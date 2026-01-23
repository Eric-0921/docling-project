---
description: Finish a feature branch with quality gates
---

1. Quality Gate: Ensure clean status.

   ```bash
   git status --porcelain
   # Should be empty. If not, commit or stash first.
   ```

2. Sync with `dev`.
   ```bash
   git checkout dev
   git pull origin dev
   ```

// turbo 3. Merge with NO fast-forward (Preserve history).

```bash
git merge --no-ff <feature_branch_name>
```

4. Push to remote.

   ```bash
   git push origin dev
   ```

5. Cleanup local branch.

   ```bash
   git branch -d <feature_branch_name>
   ```

6. Notify user: Feature merged and pushed.
