---
chapter_index: 1596
title: "[:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:POINts_<P"
--- 

# [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:POINts_<P

[:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:POINts <Points>

Determines the number of steps for the LF frequency sweep within the sweep range.

This parameter always applies to the currently set sweep spacing and correlates with the step size as follows:

for linear sweeps and f STARt < f STOP freq_points = (f SPAN / step_lin) + 1 with f SPAN = f STOP - f STARt To determine the step size, use the command SWE:STEP[:LIN] .

logarithmic sweeps and f STARt < f STOP freq_points = ((log f STOP - log f STARt ) / log step_log) + 1 To determine the logarithmic step size, use the command SWE:STEP:LOG .

If you change the number of sweep points, the step size changes accordingly. The sweep range remains the same.

Each sweep spacing mode has assigned the POINts setting separately. Thus, the command refers always to the particular set mode, see [:SOURce<hw>]:LFOutput: SWEep[:FREQuency]:SPACing .

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

359

R&S ® SMB100A

Remote Control Commands

Parameters:

<Points>

integer

Range:

2

Example:

LFO:FREQ:STAR

sets the start frequency to 2 kHz.

LFO:FREQ:STOP

sets the stop frequency to 20 kHz

LFO:SWE:SPAC LIN

sets linear sweep spacing.

LFO:SWE:POIN 11

sets 11 sweep steps for linear sweep spacing. The sweep step width ( STEP ) is automatically set to 2 kHz.

