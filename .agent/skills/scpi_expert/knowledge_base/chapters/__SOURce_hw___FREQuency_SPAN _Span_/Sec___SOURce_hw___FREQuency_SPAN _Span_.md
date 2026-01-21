# [:SOURce<hw>]:FREQuency:SPAN <Span>
Determines the extent of the frequency sweep range. This setting in combination with the center frequency setting ( [:SOURce<hw>]:FREQuency:CENTer ) defines the sweep range.

This parameter is related to the start and stop frequencies. If you change the frequency, the span changes accordingly.

f SPAN = f STOP - f STARt

Operating Manual 1407.0806.32 ─ 23

350

R&S ® SMB100A

Remote Control Commands

f STARt > f STOP is permitted.

Parameters:

<Span>

float

Range:

full frequency range

Increment:

see the data sheet: RF characteristics > Resolution of setting

*RST:

400E6

Example:

FREQ:CENT 400 MHz

sets the center frequency of the frequency sweep to 400 MHz. FREQ:SPAN 200 MHz

sets a span of 200 MHz. This sets the sweep range to 300 MHz to 500 MHz.

Manual operation:

See "Span - Frequency Sweep" on page 184

