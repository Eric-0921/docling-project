# [:SOURce<hw>]:CORRection:DEXChange:EXECute
Starts the export or import of the selected file. When import is selected, the ASCII file is imported as user correction list. When export is selected, the user correction list is exported into the selected ASCII file.

Example:

CORR:DEXC:MODE IMP

selects that ASCII files with frequency and level value pairs are imported and transferred into user correction lists.

CORR:DEXC:AFIL:SEL '/var/user/import_ucor.csv' selects that ASCII file ucor.csv is imported.

CORR:DEXC:SEL '/var/user/import_ucor_imp'

selects that the ASCII file ucor.csv is imported into user cor- rection list ucor_imp . CORR:DEXC:EXEC

starts the import of the ASCII file data into the user correction file.

Usage:

Event

Manual operation:

See "Import / Export - User Correction" on page 164

