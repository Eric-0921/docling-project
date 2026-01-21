# :STATus:QUEStionable:PTRansition <PTransition>
Sets the bits of the NTRansition part of the STATus:QUEStionable register. If a bit is set, a transition from 1 to 0 in the condition part causes an entry to be made in the EVENt part of the register.


## Parameters:
<PTransition>

string

Example:

STAT:QUES:PTR 32767

all transitions from 0 to 1 in the condition part of the STA- Tus:QUEStionable register cause an entry to be made in the EVENt part

