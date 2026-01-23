---
chapter_index: 753
title: "Example:"
--- 

# Example:

Example:

SOUR:SWE:POW:MODE AUTO

TRIG:PSW:SOUR SING

SOUR:POW:MODE SWE

SOUR:SWE:POW:EXEC

"Single"

RF Block

Operating Manual 1407.0806.32 ─ 23

188

R&S ® SMB100A

Instrument Function

"Step"

"Extern Single"

"Extern Step"

Sets a step-by-step sweep cycle.

If this mode is activated, the cursor moves to the value displayed for "Current Level". Each sweep step is triggered by a variation of the value in the "Current Level" entry window. The step width is set below at entry field "Step".

If this mode is activated, the cursor moves to the value displayed for "Current Level". If a different sweep mode was activated prior to the "Step" mode, the current sweep is stopped. The step sweep starts at the current level value.

