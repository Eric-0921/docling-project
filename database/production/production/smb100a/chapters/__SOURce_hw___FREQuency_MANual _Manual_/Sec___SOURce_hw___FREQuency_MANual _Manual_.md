# [:SOURce<hw>]:FREQuency:MANual <Manual>
Determines the frequency and triggers a sweep step manually in SWE:MODE MAN .

Note: You can select any frequency within the setting range. The range is defined with the parameters [:SOURce<hw>]:FREQuency:STARt and [:SOURce<hw>]: FREQuency:STOP . A defined offset and the multiplier factor affect the sweep range and therefore all correlated parameters. The set frequencies are only absolute values, if the offset = 0 and the multiplication factor = 1. The multiplier multiplies the frequencies accordingly, and the offset ≠ 0 shifts the frequencies corresponding to the set value.

f STARt * f MULTiplier + f OFFset ... f STOP * f MULTiplier + f OFFset

Operating Manual 1407.0806.32 ─ 23

348

R&S ® SMB100A

Remote Control Commands

