---
chapter_index: 1922
title: "[:SOURce<hw>]:SWEep[:FREQuency]:POINts_<Points>"
--- 

# [:SOURce<hw>]:SWEep[:FREQuency]:POINts_<Points>

[:SOURce<hw>]:SWEep[:FREQuency]:POINts <Points>

Determines the number of steps for the RF frequency sweep within the sweep range.

This parameter always applies to the currently set sweep spacing and correlates with the step size as follows:

for linear sweeps freq_points = (f SPAN / step_lin) + 1 To determine the step size, use the command SWE:STEP[:LIN] .

logarithmic sweeps and f STARt < f STOP freqq_points = ((log f STOP - log f STARt ) / log step_log) + 1 To determine the logarithmic step size, use the command SWE:STEP:LOG .

If you change the number of sweep points, the step size changes accordingly. The sweep range remains the same.

