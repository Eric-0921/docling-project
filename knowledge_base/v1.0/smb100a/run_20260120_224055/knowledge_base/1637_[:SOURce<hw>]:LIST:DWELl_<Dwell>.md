---
chapter_index: 1637
title: "[:SOURce<hw>]:LIST:DWELl_<Dwell>"
--- 

# [:SOURce<hw>]:LIST:DWELl_<Dwell>

[:SOURce<hw>]:LIST:DWELl <Dwell>

Sets the dwell time. The R&S SMB generates the signal with the frequency / power value pairs of each list entry for that particular period.

Operating Manual 1407.0806.32 ─ 23

370

R&S ® SMB100A

Remote Control Commands

Parameters:

<Dwell>

float

Range:

7E-4  to  100

Increment:

1E-4

*RST:

15E-3

Example:

LIST:DWELl 15

retains each setting in the list for 15 ms.

Manual operation:

See "Dwell Time - List Mode" on page 195

