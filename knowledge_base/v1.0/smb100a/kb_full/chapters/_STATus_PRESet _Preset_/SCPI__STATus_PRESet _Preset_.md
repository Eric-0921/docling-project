# :STATus:PRESet <Preset>
Resets the status registers. All PTRansition parts are set to FFFFh (32767), i.e. all transitions from 0 to 1 are detected. All NTRansition parts are set to 0, i.e. a transition from 1 to 0 in a CONDition bit is not detected. The ENABle parts of STATus:OPERation and STATus:QUEStionable are set to 0, i.e. all events in these registers are not passed on.


## Parameters:
<Preset>

string

Example:

STAT:PRES

resets the status registers.

