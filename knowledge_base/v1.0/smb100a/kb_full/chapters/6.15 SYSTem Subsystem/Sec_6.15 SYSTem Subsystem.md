# 6.15 SYSTem Subsystem
The SYSTem subsystem contains a series of commands for general functions which do not directly affect signal generation.

| :SYSTem:ERRor:ALL?....................................................................................................438      |
|--------------------------------------------------------------------------------------------------------------------------------|
| :SYSTem:ERRor:CODE:ALL?......................................................................................... 439           |
| :SYSTem:ERRor:CODE[:NEXT]?.....................................................................................439             |
| :SYSTem:ERRor:COUNt?...............................................................................................440         |
| :SYSTem:ERRor[:NEXT]?...............................................................................................440        |
| :SYSTem:ERRor:HISTory?..............................................................................................440        |
| :SYSTem:ERRor:HISTory:CLEar......................................................................................441           |
| :SYSTem:ERRor:STATic?............................................................................................... 441       |
| :SYSTem:HELP:EXPort.................................................................................................. 441      |
| :SYSTem:DLOCk........................................................................................................... 442   |
| :SYSTem:KLOCk........................................................................................................... 442   |
| :SYSTem:ULOCk........................................................................................................... 442   |
| :SYSTem:RCL............................................................................................................... 443 |
| :SYSTem:SAV................................................................................................................443 |
| :SYSTem:SECurity:VOLMode[:STATe]..............................................................................443              |
| :SYSTem:COMMunicate:GPIB:LTERminator.....................................................................444                   |
| :SYSTem:COMMunicate:GPIB[:SELF]:ADDRess...............................................................444                      |
| :SYSTem:COMMunicate:NETWork[:COMMon]:DOMain.....................................................444                            |
| :SYSTem:COMMunicate:NETWork[:COMMon]:HOSTname................................................445                               |
| :SYSTem:COMMunicate:NETWork[:COMMon]:WORKgroup.............................................. 445                               |
| :SYSTem:COMMunicate:NETWork[:IPADdress]:DNS.........................................................445                        |
| :SYSTem:COMMunicate:NETWork:IPADdress:MODE........................................................445                          |
| :SYSTem:COMMunicate:NETWork:IPADdress..................................................................446                     |
| :SYSTem:COMMunicate:NETWork[:IPADdress]:GATeway..................................................446                           |
| :SYSTem:COMMunicate:NETWork[:IPADdress]:SUBNet:MASK..........................................446                               |
| :SYSTem:COMMunicate:NETWork:MACaddress...............................................................446                       |
| :SYSTem:COMMunicate:NETWork:STATus?.................................................................... 447                    |
| :SYSTem:COMMunicate:NETWork:RESTart..................................................................... 447                   |
| :SYSTem:NINFormation?................................................................................................447       |
| :SYSTem:COMMunicate:GPIB:RESource?.......................................................................447                   |
| :SYSTem:COMMunicate:NETWork:RESource?.................................................................448                      |
| :SYSTem:COMMunicate:HISLip:RESource?.....................................................................448                   |
| :SYSTem:COMMunicate:USB:RESource?........................................................................448                   |
SYSTem Subsystem

Operating Manual 1407.0806.32 ─ 23

437

R&S ® SMB100A

Remote Control Commands

string

Error/event_number,"Error/event_description>[;Device-dependent info]"

A comma separated list of error number and a short description of the error in FIFO order.

If the queue is empty, the response is 0,"No error"

Positive error numbers are instrument-dependent. Negative error numbers are reserved by the SCPI standard.

Volatile errors are reported once, at the time they appear. Identical errors are reported repeatedly only if the original error has already been retrieved from (and hence not any more present in) the error queue.

