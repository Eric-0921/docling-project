# :STATus:OPERation:NTRansition <Ntransition>
Sets the bits of the NTRansition part of the STATus:OPERation register. If a bit is set, a transition from 1 to 0 in the condition part causes an entry to be made in the EVENt part of the register. The disappearance of an event in the hardware is thus registered, for example the end of an adjustment.


## Parameters:
<Ntransition>

string

Example:

:STAT:OPER:NTR 0

a transition from 1 to 0 in the condition part of the Status:Opera- tion register does not cause an entry to be made in the EVENt part.

STATus subsystem

Operating Manual 1407.0806.32 ─ 23

434

R&S ® SMB100A

Remote Control Commands

STATus subsystem

