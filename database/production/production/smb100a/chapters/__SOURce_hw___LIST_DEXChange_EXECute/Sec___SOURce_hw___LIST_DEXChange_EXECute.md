# [:SOURce<hw>]:LIST:DEXChange:EXECute
Executes the import or export of the selected list file, according to the previously set transfer direction with command [:SOURce<hw>]:LIST:DEXChange:MODE .

Example:

LIST:DEXC:MODE IMP

determines that ASCII files with frequency and level value pairs are imported into list mode lists.

LIST:DEXC:AFIL:SEL '/var/list.csv'

selects the ASCII file list.csv for import.

LIST:DEXC:SEL '/var/list_imp'

determines the destination file list_imp .

LIST:DEXC:EXEC

imports the ASCII file data into the list mode file.

Usage:

Event

Manual operation:

See "Import / Export - List Mode" on page 200

Operating Manual 1407.0806.32 ─ 23

369

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

