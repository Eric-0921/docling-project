# [:SOURce<hw>]:FREQuency:STOP <Stop>
Sets the stop frequency for the RF sweep.

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

351

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

This parameter is related to the center frequency and span. If you change the frequency, these parameters change accordingly.

f STARt > f STOP is permitted.

f STOP = (f CENTer + f SPAN /2).

Note: A defined offset affects the sweep range and consequently all correlating parameters. The set frequencies are only absolute values, if the Offset = 0. Offset ≠ 0 shifts the frequencies according to the offset value.

f STARt * f MULTiplier + f OFFSet ... f STOP * f MULTiplier + f OFFSet

