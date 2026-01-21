# :SYSTem:WAIT <TimeMs>
Delays the execution of the subsequent remote command by the specified time.

This function is useful, for example to execute an SCPI sequence automatically but with a defined time delay between some commands.


## Setting parameters:
<TimeMs>

integer

Wait time in ms

Range:

0  to  10000

*RST:

0

Example:

:SYSTem:WAIT 10000

// waits 10s before resetting the instrument

*RST

Usage:

Setting only

