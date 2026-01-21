# [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:STEP[:LINear] <Linear>
Sets the step size for linear LF frequency sweep steps.

Operating Manual 1407.0806.32 ─ 23

361

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

This parameter correlates with the number of steps [:SOURce<hw>]:LFOutput: SWEep[:FREQuency]:POINts within the sweep range as follows:

f STARt < f STOP

\ f r e q \_ p i n t s = ( ( f _ { S T A R t } - f _ { S T O P } ) / \, \text {step} \_ \sin ) + 1

If you change the step size, the number of steps changes accordingly. The sweep range remains the same.

