# [:SOURce<hw>]:CORRection:DEXChange:MODE <Mode>
Selects if user correction lists should be imported or exported. Depending on the selection her, the file select command define either the source or the destination for user correction lists and ASCII files.

Parameters:

<Mode>

IMPort | EXPort

*RST:

IMPort

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

340

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

Example:

CORR:DEXC:MODE IMP

selects that ASCII files with frequency and level value pairs are imported and transferred into user correction lists.

CORR:DEXC:AFIL:SEL '/var/user/ucor.csv'

selects that ASCII file ucor.csv is imported.

CORR:DEXC:SEL '/var/user/ucor_imp'

selects that the ASCII file ucor.csv is imported into user cor- rection list ucor_imp .

Manual operation:

See "Mode - User Correction" on page 163

