---
chapter_index: 709
title: "Example:"
--- 

# Example:

Example:

SOUR:SWE:FREQ:MODE AUTO

TRIG:FSW:SOUR SING

SOUR:FREQ:MODE SWE

SOUR:SWE:FREQ:EXEC

Operating Manual 1407.0806.32 ─ 23

181

R&S ® SMB100A

Instrument Function

RF Block

"Step"

"Extern Single"

Generates the sweep signal step-by-step, manually triggered. To perform the sweep steps, enter the frequency value under Current Freq - Frequency Sweep. You can directly enter the value, but also use the [up] and [down] navigation keys or the [rotary knob]. You can determine the step width below in the entry field "Step Lin" or "Step Log", see Step Lin/Log - Frequency Sweep. If a step is out of the sweep range ("Start Freq" or "Stop Freq"), it is ignored.

Note: To step through the sweep frequencies in remote control mode, use the FREQ:MAN command with the UP or DOWN parameter.

