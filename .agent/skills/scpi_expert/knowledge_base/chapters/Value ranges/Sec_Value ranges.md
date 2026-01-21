# Value ranges
Queries return the current value of the respective register, which permits a check of the device status.

Return values: A decimal value in the range 0 to 32767 (=2 15 -1)

The configuration commands set the respective register thus determining which status changes of the R&S SMB cause the status registers to be changed. Setting values: A decimal value in the range 0 to 32767 (=2 15 -1)

| :STATus:OPERation:CONDition?.....................................................................................434          |
|-------------------------------------------------------------------------------------------------------------------------------|
| :STATus:OPERation:ENABle...........................................................................................434        |
| :STATus:OPERation[:EVENt]...........................................................................................434       |
| :STATus:OPERation:NTRansition.................................................................................... 434         |
| :STATus:OPERation:PTRansition.....................................................................................435         |
| :STATus:PRESet............................................................................................................435 |
| :STATus:QUEStionable:CONDition.................................................................................. 435          |
| :STATus:QUEStionable:ENABle.......................................................................................435         |
| :STATus:QUEStionable[:EVENt]...................................................................................... 436        |
| :STATus:QUEStionable:NTRansition................................................................................436           |
| :STATus:QUEStionable:PTRansition................................................................................ 436          |
| :STATus:QUEue[:NEXT]?................................................................................................436      |
STATus subsystem

Operating Manual 1407.0806.32 ─ 23

433

R&S ® SMB100A

Remote Control Commands

