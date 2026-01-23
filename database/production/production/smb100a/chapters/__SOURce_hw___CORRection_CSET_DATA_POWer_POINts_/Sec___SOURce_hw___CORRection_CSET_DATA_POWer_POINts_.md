# [:SOURce<hw>]:CORRection:CSET:DATA:POWer:POINts?
Queries the number of level values in the selected table.

The numerical suffix at SOURce must not be used for this command.

Operating Manual 1407.0806.32 ─ 23

336

R&S ® SMB100A

Remote Control Commands

Return values:

<Points>

integer

Range:

0  to  10000

*RST:

0

Example:

CORR:CSET '/var/user/ucor1'

selects the table ucor1.

CORR:CSET:DATA:POW:POIN?

queries the number of level values in the table ucor1.

Response:

440

the table ucor1 contains 440 level values.

Usage:

Query only

