# :STATus:OPERation:PTRansition <Ptransition>
Sets the bits of the PTRansition part of the STATus:OPERation register. If a bit is set, a transition from 0 to 1 in the condition part causes an entry to be made in the EVENt part of the register. A new event in the hardware is thus registered, for example the start of an adjustment.


## Parameters:
<Ptransition>

string

Example:

:STAT:OPER:PTR 32767

all transitions from 0 to 1 in the condition part of the Status:Oper- ation register cause an entry to be made in the EVENt part.

