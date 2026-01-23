# :HCOPy:FILE[:NAME]:AUTO[:FILE]:NUMBer?
Queries the number that is used as part of the file name for the next hard copy in automatic mode.

At the beginning, the count starts at 0. The R&S SMB searches the specified output directory for the highest number in the stored files. It increases this number by one to achieve a unique name for the new file.

The resulting auto number is appended to the resulting file name with at least three digits.

Operating Manual 1407.0806.32 ─ 23

302

R&S ® SMB100A

Remote Control Commands


## Return values:
<Number>

integer

Range:

0  to  999999

*RST:

0

Example:

See Example "Store a hard copy of the display" on page 299.

Usage:

Query only

Manual operation:

See "File Options" on page 125

