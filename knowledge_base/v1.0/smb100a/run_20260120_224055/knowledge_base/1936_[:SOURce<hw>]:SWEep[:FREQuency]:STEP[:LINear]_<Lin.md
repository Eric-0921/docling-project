---
chapter_index: 1936
title: "[:SOURce<hw>]:SWEep[:FREQuency]:STEP[:LINear]_<Lin"
--- 

# [:SOURce<hw>]:SWEep[:FREQuency]:STEP[:LINear]_<Lin

[:SOURce<hw>]:SWEep[:FREQuency]:STEP[:LINear] <Linear>

Sets the step size for linear RF frequency sweep steps.

This parameter is related to the number of steps ( [:SOURce<hw>]:SWEep[: FREQuency]:POINts ) within the sweep range as follows:

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

427

R&S ® SMB100A

Remote Control Commands

f STARt < f STOP

freq_points = (f SPAN / step_lin) + 1

If you change the step size, the number of steps changes accordingly. The sweep range remains the same.

The keywords [:FREQuency] and [:LINear] can be omitted. The command is then SCPI-compliant.

Parameters:

<Linear>

float

Range:

full frequency range

Increment:

see the data sheet: RF characteristics > Resolution of setting

Example:

FREQ:STAR 1GHz

sets the start frequency to 1 GHz.

FREQ:STOP 5GHz

sets the stop frequency to 5 GHz.

SWE:SPAC LIN

sets linear sweep spacing.

SWE:STEP 2 MHz

sets the step width for linear sweep spacing to 2 MHz (RF sweep) at the RF output. The number of sweep steps for linear sweep spacing ( POINts ) is automatically set to 2001.

Manual operation:

See "Step Lin/Log - Frequency Sweep" on page 185

