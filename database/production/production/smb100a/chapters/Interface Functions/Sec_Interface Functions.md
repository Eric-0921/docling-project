# Interface Functions
Instruments which can be controlled via GPIB bus can be equipped with different interface functions. The interface function for the R&S SMB are listed in the following table.

| Control character   | Interface function                                                                      |
|---------------------|-----------------------------------------------------------------------------------------|
| SH1                 | Handshake source function (source handshake), full capability                           |
| AH1                 | Handshake sink function (acceptor handshake), full capability                           |
| L4                  | Listener function, full capability, de-addressed by MTA.                                |
| T6                  | Talker function, full capability, ability to respond to serial poll, deaddressed by MLA |
| SR1                 | Service request function (Service Request), full capability                             |
| PP1                 | Parallel poll function, full capability                                                 |
| RL1                 | Remote/Local switch over function, full capability                                      |
| DC1                 | Reset function (Device Clear), full capability                                          |
| DT1                 | Trigger function (Device Trigger), full capability                                      |
Operating Manual 1407.0806.32 ─ 23

509

R&S ® SMB100A

List of commands

