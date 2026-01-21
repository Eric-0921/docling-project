---
description: Commit changes using Conventional Commits standard
---

1. Check changed files with `git status`.
2. Add all relevant changes: `git add .` (or specific files if requested).
3. Generate a commit message following the pattern `<type>(<scope>): <subject>`.
   - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
   - Scope: The module affected (e.g., `parser`, `lockin`, `smb100a`).
   - Subject: Concise description of the change.
4. Execute the commit:
   ```bash
   git commit -m "<generated_message>"
   ```
5. Update CHANGELOG.md:
   - Append the commit message to the `## [Unreleased]` section of `CHANGELOG.md`.
   - Format: `- <generated_message> (SHA: <short_sha>)`
   ```bash
   echo "- <generated_message>" >> CHANGELOG.md
   # Optional: Commit the changelog update (amend or new commit)
   git add CHANGELOG.md
   git commit --amend --no-edit
   ```
6. Push the branch to remote (if applicable):
   ```bash
   git push -u origin HEAD
   ```
