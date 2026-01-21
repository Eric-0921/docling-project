# [:SOURce<hw>]:CORRection:DEXChange:AFILe:SEParator:DECimal <Decimal>
Selects the decimal separator used in the ASCII data between '.' (decimal point) and ',' (comma) with floating-point numerals.

Operating Manual 1407.0806.32 ─ 23

339

R&S ® SMB100A

Remote Control Commands

Parameters:

<Decimal>

DOT | COMMa

*RST:

DOT

Example:

CORR:DEXC:MODE EXP

selects that the user correction list is exported into an ASCII file.

CORR:DEXC:AFIL:SEL '/var/user/import_ucor.csv'

selects ASCII file ucor.csv as destination for the user correction list data.

CORR:DEXC:AFIL:SEP:COL TAB

the pairs of frequency and level values are separated by a tabu- lator.

CORR:DEXC:AFIL:SEP:DEC DOT

selects the decimal separator dot.

CORR:DEXC:SEL '/var/user/import_ucor_imp'

selects that the user correction list ucor_imp is imported into ASCII file ucor.csv .

Manual operation:

See "Decimal Point - User Correction" on page 163

