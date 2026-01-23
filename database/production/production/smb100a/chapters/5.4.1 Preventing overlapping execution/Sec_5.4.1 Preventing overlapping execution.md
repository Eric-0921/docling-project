# 5.4.1 Preventing overlapping execution
To prevent an overlapping execution of commands, one of the commands *OPC , *OPC? or *WAI can be used. All three commands cause a certain action only to be carried out after the hardware has been set. The controller can be forced to wait for the corresponding action to occur.

| Com- mand   | Action                                                                                                                        | Programming the controller                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| *OPC        | Sets the Operation Complete bit in the Stan- dard Event Status Register (ESR) after all previous commands have been executed. | ● Setting bit 0 in the ESE ● Setting bit 5 in the SRE ● Waiting for service request (SRQ)                        |
| *OPC?       | Stops command processing until 1 is returned. This occurs when all pending opera- tions are completed.                        | Send *OPC? directly after the command whose processing must be terminated before other commands can be executed. |
| *WAI        | Stops further command processing until all commands sent before Wait-to-Continue Command (WAI) have been executed.            | Send *WAI directly after the command whose processing must be terminated before other commands are executed.     |
Command synchronization using *WAI or *OPC? is a good choice if the overlapped command takes only little time to process. The two synchronization commands simply block overlapping execution of the command. Append the synchronization command to the overlapped command, for example:

SINGle;	*OPC?

For time consuming overlapped commands, you can allow the controller or the instrument to do other useful work while waiting for command execution. Use one of the following methods:

