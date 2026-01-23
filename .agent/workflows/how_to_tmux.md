---
description: How to use Tmux for persistent sessions
---

# Tmux Cheatsheet

## Core Commands

| Command                       | Description                   |
| :---------------------------- | :---------------------------- |
| `tmux new -s <name>`          | Create a new named session    |
| `tmux ls`                     | List all running sessions     |
| `tmux attach -t <name>`       | Attach to an existing session |
| `tmux kill-session -t <name>` | Kill a specific session       |

## Inside Tmux (Prefix: `Ctrl+B`)

- **Detach (Keep Running)**: `Ctrl+B` then `d`
- **New Window**: `Ctrl+B` then `c`
- **Next Window**: `Ctrl+B` then `n`
- **Previous Window**: `Ctrl+B` then `p`
- **Scroll Mode**: `Ctrl+B` then `[` (Use arrows/PgUp/PgDn, `q` to quit)

## Common Workflows

### Running Long Tasks (e.g. Translation)

1. `tmux new -s translation_job`
2. `conda activate doclingprj1`
3. Run script: `python main.py`
4. Detach: `Ctrl+B` `d`
5. (Optional) Logout SSH
6. Re-login and Check: `tmux attach -t translation_job`

### Recovering Session

1. `tmux ls` to find session name.
2. `tmux attach -t <name>`
