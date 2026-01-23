---
description: Project directory structure and file naming conventions
---

# Project Structure & Naming Rules

## 1. Directory Structure

The project follows a Monorepo structure separating "Data Production" from "Instrument Control".

```text
project-root/
├── .agent/                 # Agent configuration, rules, skills, workflows
├── references/             # External references (e.g., official examples)
├── docling_pipeline/       # [Module 1] Knowledge Base Production (PDF Processing)
│   ├── input/              # Raw PDF sources
│   ├── scripts/            # Docling conversion scripts
│   └── config/             # OCR/Table extraction config
├── database/               # Data Storage
│   ├── production/         # PROD Knowledge Base (Clean, Git-Tracked)
│   │   ├── i18n/           # Translated manuals
│   │   └── raw/            # Raw text references
│   ├── visual_optimized/   # AI-optimized manual versions
│   └── raw/                # Original source files
├── experimental_data/      # [Git-Ignored] Logs, raw captures, scratchpad
├── instrument_control/     # [Module 3] Control Code
│   ├── drivers/            # Low-level drivers
│   └── experiments/        # Experiment scripts
├── docs/                   # Human Documentation (Guides, Planning, Archive)
└── ai_adapter/             # AI Integration logic (Translation Agents, etc.)
```

## 2. File Safety & Naming

- **Path Names**: MUST be English/ASCII only. No Chinese characters in filenames.
- **Production Data**: `database/production/` contains verified knowledge. Do not modify manually without caution.
- **Experimental Data**: Output limited to `experimental_data/`.
  - **Rule**: Any new data directory created MUST be verified against `.gitignore` first. Do not commit large logs (>10MB).
