# :SENSe<ch>[:POWer]:FILTer:LENGth[:USER] <User>
The command selects the filter length for user filter mode

( SENSe:POWer:FILTer:TYPE USER ). As the filter length works as a multiplier for the time window, a constant filter length results in a constant measurement time. Values 1 and 2^n are settable.

The time window is fixed to 20 ms.

Parameters:

<User>

float

Range:

1  to  65536

*RST:

1

Example:

SENS:FILT:TYPE USER

selects user filter mode.

SENS:FILT:LENG 16

sets a filter length of 16. The resulting measurement time is 640 ms (2x16x20 ms).

Manual operation:

See "Filter Length" on page 176

