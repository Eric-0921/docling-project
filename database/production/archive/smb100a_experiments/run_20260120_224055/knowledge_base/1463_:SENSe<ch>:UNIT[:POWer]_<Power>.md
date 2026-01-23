---
chapter_index: 1463
title: ":SENSe<ch>:UNIT[:POWer]_<Power>"
--- 

# :SENSe<ch>:UNIT[:POWer]_<Power>

:SENSe<ch>:UNIT[:POWer] <Power>

The command selects the unit used for result query with command READ. The power sensor provides the measured value in Watt. In which unit the measured value is returned is selected here and might be either Watt, dBm or dBuV.

Parameters:

<Power>

DBM | DBUV | WATT

*RST:

DBM

Example:

SENS2:UNIT DBM

selects unit dBm for the measured value returned by command READ .

READ2?

Response: 7.34

7.34 dBm are measured by sensor 2.

Manual operation:

See "Unit" on page 174

