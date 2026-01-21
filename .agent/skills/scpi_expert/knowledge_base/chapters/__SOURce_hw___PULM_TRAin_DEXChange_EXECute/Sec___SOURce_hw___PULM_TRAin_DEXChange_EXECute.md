# [:SOURce<hw>]:PULM:TRAin:DEXChange:EXECute
Starts the export or import of the selected file. When import is selected, the ASCII file is imported as pulse train list. When export is selected, the pulse train list is exported into the selected ASCII file.

Example:

PULM:TRA:DEXC:MODE IMP

selects that ASCII files with ontime/offtime/repetition values are imported and transferred into pulse train lists.

MMEM:CDIR '/var/user/Lists/import'

selects the directory for the ASCII files with on-time/off-time/ repetition values.

PULM:TRA:DEXC:AFIL:SEL 'train.csv'

selects that ASCII file train.csv is imported.

PULM:TRA:DEXC:SEL 'train_imp'

selects that the ASCII file train.csv is imported into pulse

train list train_imp .

PULM:TRA:DEXC:EXEC

starts the import of the ASCII file data into the pulse train file.

Usage:

Event

Options:

R&S SMB-K27 (Pulse Train)

Manual operation:

See "Import / Export - Import/Export Pulse Train Files" on page 239

