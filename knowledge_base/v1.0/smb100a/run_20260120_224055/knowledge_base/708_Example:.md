---
chapter_index: 708
title: "Example:"
--- 

# Example:

Example:

SOUR:SWE:FREQ:MODE AUTO

TRIG:FSW:SOUR AUTO

SOUR:FREQ:MODE SWE

Generates a single sweep cycle after a trigger event.

The sweep steps within the cycle are performed automatically, controlled by the dwell time. If one cycle is completed, the instrument waits for the next trigger event.

To trigger the sweep, use "Execute Single Sweep" button, or the corresponding remote control commands, for example *TRG .

