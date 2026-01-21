# :SYSTem:COMMunicate:GPIB:RESource?
Queries the VISA resource string for remote control via the GPIB interface.

To change the GPIB address, use the command :SYSTem:COMMunicate:GPIB[: SELF]:ADDRess .


## Return values:
<Resource>

string

Example:

SYSTem:COMMunicate:GPIB:RESource?

queries the VISA resource string.

Response: "GPIB::28::INSTR" '

Usage:

Query only

SYSTem Subsystem

Operating Manual 1407.0806.32 ─ 23

447

R&S ® SMB100A

Remote Control Commands

Manual operation:

See "VISA Resource Strings" on page 110

