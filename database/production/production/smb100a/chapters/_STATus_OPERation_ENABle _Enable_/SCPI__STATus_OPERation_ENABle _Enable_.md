# :STATus:OPERation:ENABle <Enable>
Sets the bits of the ENABle part of the STATus:OPERation register. This setting determines which events of the Status-Event part are forwarded to the sum bit in the status byte. These events can be used for a service request.


## Parameters:
<Enable>

string

Example:

:STAT:OPER:ENAB 32767

all events are forwarded to the sum bit of the status byte.

