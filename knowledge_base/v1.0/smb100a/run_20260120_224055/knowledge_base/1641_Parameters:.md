---
chapter_index: 1641
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Frequency>

<Frequency#1>{, <Frequency#2>,

The data can be given either as a list of numbers (list can be of any length and list entries must be separated by commas) or as binary block data. When block data is transferred, 8 bytes are always interpreted as a floating-point number with double accu- racy (see :FORMat[:DATA] on page 298).

Range:

300 kHz  to  RFmax

Example:

LIST:SEL '/var/list3'

selects list3 for editing. The R&S SMB generates a new file automatically, if it does not exist yet.

SOUR:LIST:FREQ 1.4GHz, 1.3GHz, 1.2GHz,

specifies the frequency values in list3. If the list already contains data, it is overwritten.

Manual operation:

See "Edit List Mode Data

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

371

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

