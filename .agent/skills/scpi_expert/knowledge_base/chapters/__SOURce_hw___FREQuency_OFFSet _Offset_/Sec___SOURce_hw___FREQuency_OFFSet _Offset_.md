# [:SOURce<hw>]:FREQuency:OFFSet <Offset>
Sets the frequency offset of a downstream instrument, for example a mixer.

If you have specified an OFFSet and / or a MULTiplier factor, the actual frequency at the RF output does not change, but rather the value queried with [:SOUR]:FREQ? , according to the following formula:

f FREQ = f RFout * f MULTiplier + f OFFSet

