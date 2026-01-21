---
chapter_index: 1824
title: "Return_values:"
--- 

# Return_values:

Return values:

<Catalog>

string

Example:

MMEM:CDIR '/var/user/Lists/import'

selects the directory for the ASCII files with ontime/offtime/repe- tition values.

PULM:TRA:DEXC:AFIL:EXT TXT

selects that ASCII files with extension *.txt are listed.

PULM:TRA:DEXC:AFIL:CAT?

queries the available files with extension *.txt .

Response: 'train1','train2'

the ASCII files train1.txt and train2.txt are available.

Usage:

Query only

Options:

R&S SMB-K27 (Pulse Train)

Manual operation:

See "Select ASCII Source / Destination - Import/Export Pulse Train Files" on page 239

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

405

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

