---
chapter_index: 1584
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Start>

float

Range:

full frequency range

Increment:

see the data sheet: Resolution of frequency setting

*RST:

1 KHz

Example:

RST*

activates all presettings.

LFO:SWE:MODE AUTO

TRIG0:SOUR SING

LFO:FREQ:STAR 1 kHz

LFO:FREQ:STOP 10 kHz

LFO:FREQ:MODE SWE

LFO:SWE:EXEC

the instrument generates a single sweep cycle from 1 kHz to 10

kHz automatically after a manual trigger event occurs ( :LFOutput:SWEep:EXECute or *TRG ). The step width is 1 kHz linear, with 15 ms dell time until the signal switches to the subsequent step.

Manual operation:

See "Start Freq" on page 229

