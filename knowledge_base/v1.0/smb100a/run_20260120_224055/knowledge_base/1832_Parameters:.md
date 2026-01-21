---
chapter_index: 1832
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Decimal>

DOT | COMMa

*RST:

DOT

Example:

PULM:TRA:DEXC:MODE EXP

selects that the pulse train list is exported into an ASCII file. MMEM:CDIR '/var/user/Lists/import'

selects the directory for the ASCII files with on-time/off-time/ repetition values.

PULM:TRA:DEXC:AFIL:SEL 'train.csv'

selects ASCII file train.csv as destination for the pulse train list data.

PULM:TRA:DEXC:AFIL:SEP:COL TAB

the ontime/offtime/repetition values are separated by a tabulator.

PULM:TRA:DEXC:AFIL:SEP:DEC DOT

selects the decimal separator dot.

PULM:TRA:DEXC:SEL 'train_imp'

selects that the pulse train list

train_imp

is imported into

ASCII file train.csv .

Options:

R&S SMB-K27 (Pulse Train)

Operating Manual 1407.0806.32 ─ 23

407

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

Manual operation:

See "Decimal Point - ASCII File Settings" on page 239

