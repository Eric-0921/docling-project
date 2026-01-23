---
chapter_index: 1947
title: "[:SOURce<hw>]:SWEep:POWer:POINts_<Points>"
--- 

# [:SOURce<hw>]:SWEep:POWer:POINts_<Points>

[:SOURce<hw>]:SWEep:POWer:POINts <Points>

Determines the number of steps for the RF level sweep within the sweep range.

This parameter always applies to the currently set sweep spacing and correlates with the step size as follows:

pow_points = (f STOP - f STARt / step_log) + 1

To determine the step size use the command SWE:POW:STEP[:LOG] .

If you change the number of sweep points, the step size changes accordingly. The sweep range remains the same.

