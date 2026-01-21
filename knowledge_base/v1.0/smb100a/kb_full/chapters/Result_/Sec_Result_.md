# Result:
1000000000 (1 GHz)

Whereas the result for the following commands is not specified by SCPI:

:FREQ:STAR 1GHz;STAR?;SPAN 1000000

The result could be the value of STARt before the command was sent since the instrument can defer executing the individual commands until a program message terminator is received. The result could also be 1 GHz if the instrument executes commands as they are received.

As a general rule, send commands and queries in different program messages.

Operating Manual 1407.0806.32 ─ 23

271

R&S ® SMB100A

Remote Control Basics

