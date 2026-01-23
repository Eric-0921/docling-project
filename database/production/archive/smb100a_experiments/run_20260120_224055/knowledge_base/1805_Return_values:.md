---
chapter_index: 1805
title: "Return_values:"
--- 

# Return_values:

Return values:

<Points>

integer

Range:

0  to  2047

*RST:

0

Example:

MMEM:CDIR '/var/user/Lists'

selects the directory for the pulse train files.

PULM:TRA:SEL 'P_INCR'

selects P_INCR for editing. P_INCR is created if it does not yet exist.

PULM:TRA:ONT:POIN?

queries the number of frequency values in P_INCR

Response: 7

P_INCR has 7 ontime entries.

Usage:

Query only

Options:

R&S SMB-K27 (Pulse Train)

