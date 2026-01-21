# [:SOURce<hw>]:SWEep[:FREQuency]:STEP:LOGarithmic <Logarithmic>
Sets a logarithmically determined sweep step size for the RF frequency sweep. It is expressed in percent and you must enter the value and the unit PCT with the command.

The frequency is increased by a logarithmically calculated fraction of the current frequency according to:

\begin{array} { r l } { s t e p _ { - } \log _ { n + 1 } = f _ { n } + s t e p _ { - } \log _ { n } \times f _ { n } } \end{array}

f _ { n + 1 } = f _ { n } + \text {step} \_ \log _ { n + 1 }

with f STARt < f STOP and n = number of sweep steps

This parameter correlates with the number of steps SWE:FREQ:POIN within the sweep range as follows:

freq_points = ((log f STOP - log f STARt ) / log step_log) + 1

If you change the step size, the number of steps changes accordingly. The sweep range remains the same.

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

428

R&S ® SMB100A

Remote Control Commands

