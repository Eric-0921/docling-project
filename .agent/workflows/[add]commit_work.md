---
description: Commit changes using Conventional Commits standard (Turbo Mode)
---

1. Check workspace status.

   ```bash
   git status
   ```

2. Generate a commit message following `<type>(<scope>): <subject>` pattern.
   - Example: `feat(parser): add pdf table extraction`

3. Update CHANGELOG.md (Insert at top).
   - Use `sed` to insert the new entry right after the `## [Unreleased]` line.
   ```bash
   # Adjust '## [Unreleased]' if your changelog header differs
   sed -i '/## \[Unreleased\]/a - <generated_message>' CHANGELOG.md
   ```

// turbo-all 4. Stage all changes (including Changelog) and Commit.

```bash
git add .
git commit -m "<generated_message>"
```

5. Push (if on a feature branch).
   ```bash
   git push
   ```
