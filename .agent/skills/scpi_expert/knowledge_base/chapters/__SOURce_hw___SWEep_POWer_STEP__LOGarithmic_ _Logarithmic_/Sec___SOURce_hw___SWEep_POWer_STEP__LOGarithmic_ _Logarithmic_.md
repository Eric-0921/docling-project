# [:SOURce<hw>]:SWEep:POWer:STEP[:LOGarithmic] <Logarithmic>
Sets a logarithmically determined sweep step size for the RF level sweep. It is expressed in decibels and you must enter the value and the unit dB with the command.

The level is increased by a logarithmically calculated fraction of the current level according to:

step_size n+1 = Level n + step_size n x Level n

Level n+1 = Level n + step_size n+1

with Level STARt < level STOP , step_size = SWE:POW:STEP[:LOG] and n = number of sweep steps

This parameter correlates with the number of steps SWE:POW:POIN within the sweep range as follows:

level_points = ((Level STOP - Level STARt ) / step_size) + 1)

If you change the step size, the number of steps changes accordingly. The sweep range remains the same.

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

432

R&S ® SMB100A

Remote Control Commands

