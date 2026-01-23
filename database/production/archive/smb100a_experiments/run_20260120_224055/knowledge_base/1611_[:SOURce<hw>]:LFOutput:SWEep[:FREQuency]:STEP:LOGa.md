---
chapter_index: 1611
title: "[:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:STEP:LOGa"
--- 

# [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:STEP:LOGa

[:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:STEP:LOGarithmic <Logarithmic>

Sets the logarithmically determined sweep step size for the LF frequency sweep. It is expressed in percent and you must enter the value and the unit PCT with the command.

The frequency is increased by a logarithmically calculated fraction of the current frequency according to:

\text {step} _ { - } \log _ { \text {step} + 1 } = f _ { \text {step} } + \text {step} _ { - } \log _ { \text {step} } \times f _ { \text {step} }

f _ { s t e p + 1 } = f _ { s t e p } + \text {step} \_ \log _ { s t e p + 1 }

with f STARt < f STOP and step = the current number of the sweep steps

This parameter correlates with the number of steps LFO:SWE[:FREQ]:POIN within the sweep range as follows:

freq_points = ((log f STOP - log f STARt ) / log step_log) + 1

If you change the step size, the number of steps changes accordingly. The sweep range remains the same.

Operating Manual 1407.0806.32 ─ 23

362

R&S ® SMB100A

Remote Control Commands

