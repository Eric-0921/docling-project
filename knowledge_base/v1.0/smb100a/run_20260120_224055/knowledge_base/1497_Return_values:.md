---
chapter_index: 1497
title: "Return_values:"
--- 

# Return_values:

Return values:

<Catalog>

string

Example:

MMEM:CDIR '/var/user/import'

selects the directory for the ASCII files with frequency and level value pairs.

CORR:DEXC:AFIL:EXT TXT

selects that ASCII files with extension *.txt are listed.

CORR:DEXC:AFIL:CAT?

queries the available files with extension *.txt .

Response:

'ucor1,ucor2'

the ASCII files ucor1.txt and ucor2.txt are available.

Usage:

Query only

