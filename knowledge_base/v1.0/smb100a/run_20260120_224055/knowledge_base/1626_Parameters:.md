---
chapter_index: 1626
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Extension>

TXT | CSV

*RST: TXT

Operating Manual 1407.0806.32 ─ 23

367

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

Example:

MMEM:CDIR '/var/import'

selects the directory for the ASCII files with frequency and level value pairs.

LIST:DEXC:AFIL:EXT TXT

selects ASCII files with the extension *.txt for the query.

LIST:DEXC:AFIL:CAT?

queries the available files with extension *.txt .

Response: 'list1,list2'

the ASCII files list1.txt and list2.txt exist.

Manual operation:

See "Extension - List Mode" on page 199

