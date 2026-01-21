# [:SOURce]:ROSCillator[:INTernal]:ADJust[:STATe] <State>
Determines whether the calibrated ( OFF ) or a user-defined ( ON ) adjustment value is used for fine adjustment of the frequency.

If user-defined values are used, the instrument is no longer in the calibrated state. However, the calibration value is not changed and the instrument resumes the calibrated state after sending the com- mand :SOURce:ROSCillator:INTernal:ADJust:STATe OFF

.

Operating Manual 1407.0806.32 ─ 23

411

R&S ® SMB100A

Remote Control Commands

Parameters:

<State>

0 | 1 | OFF | ON

*RST:

n.a. (factory preset: 0)

Example:

ROSC:SOUR INT

Selects the internal source.

ROSC:ADJ ON

Activates use of a user-defined adjustment value.

ROSC:ADJ:VAL 1400

Sets the adjustment value to 1400.

Manual operation:

See "Adjustment Active" on page 145

