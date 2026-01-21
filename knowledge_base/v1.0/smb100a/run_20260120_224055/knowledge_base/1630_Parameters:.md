---
chapter_index: 1630
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Column>

TABulator | SEMicolon | COMMa | SPACe

*RST:

COMMa

Operating Manual 1407.0806.32 ─ 23

368

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

Example:

LIST:DEXC:MODE EXP

selects that the list is exported into an ASCII file.

LIST:DEXC:AFIL:SEL '/var/list.csv'

determines ASCII file list.csv as destination for the list mode list data.

LIST:DEXC:AFIL:SEP:COL TAB

defines a tabulator to separate the frequency and level values pairs.

LIST:DEXC:AFIL:SEP:DEC DOT

selects the decimal separator dot.

LIST:DEXC:SEL '/var/list_imp'

determines the source file list_imp for export into the ASCII file

list.csv .

LIST:DEXC:EXEC

exports the list file data into the ASCII file.

Manual operation:

See "Column Separator- List Mode" on page 199

