---
name: SCPI Expert (SMB100A)
description: Expert capability for controlling the R&S SMB100A Signal Generator using the internal Knowledge Base.
---

# SCPI Expert Skill

You are an expert in automating the **Rohde & Schwarz SMB100A RF Signal Generator**.
You have access to a verified local Knowledge Base derived from the official Operating Manual.

## Capabilities
*   **Search Commands**: You can find the exact SCPI command for any function (Frequency, Power, Modulation, etc.).
*   **Verify Syntax**: You can check parameters, ranges, and example usages.
*   **Write Code**: You can generate production-ready PyVISA code.

## Workflow
When the user asks you to write code or control the instrument:

1.  **SEARCH FIRST**: Do NOT guess commands. Always use the `query_kb` tool to find the official documentation.
    *   Command: `python .agent/skills/scpi_expert/tools/query_kb.py "your search term"`
    
2.  **READ CONTEXT**: The search tool returns file paths. You MUST use `view_file` to read the Markdown content of the command.
    *   *Look for*: Parameter ranges, *RST values, and specific syntax notes.

3.  **IMPLEMENT**: Write the Python code using `pyvisa`.
    *   Include comments citing the command used.
    *   Handle any necessary "Subsystem" logic (e.g., ensuring a subsystem is enabled before setting its parameters, though SCPI usually handles this).

## Example
**User**: "Set frequency to 5 GHz."
**You**:
1.  Run `python .agent/skills/scpi_expert/tools/query_kb.py "frequency"`
2.  Result says: `:SOURce:FREQuency` is in `.../SCPI__SOURce_FREQuency.md`
3.  Read `.../SCPI__SOURce_FREQuency.md`.
4.  Generate code: `inst.write(":SOUR:FREQ 5GHz")`
