# [:SOURce<hw>]:SWEep[:FREQuency]:LFConnector <LfConnector>
Activates the output of a sweep voltage ramp at the LF connector.

The voltage range is set with commands

SOURce:SWEep:FREQuency:OVOLtage:STARt and …:STOP

Parameters:

<LfConnector>

0 | 1 | OFF | ON

*RST: 0

Example:

SWE:LFC ON

activates the output of a linear voltage ramp from sweep start to sweep stop at the LF connector.

SWE:OVOL:STAR 0V

SWE:OVOL:STOP 3V

'the voltage at sweep start is 0 Volt and at sweep stop 3 V.

Manual operation:

See "Use LF connector to output sweep voltage - RF Frequency Sweep" on page 186

Operating Manual 1407.0806.32 ─ 23

423

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

