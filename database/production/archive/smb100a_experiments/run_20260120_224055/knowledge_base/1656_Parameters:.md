---
chapter_index: 1656
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Power>

<Power#1>{, <Power#2>,

The data can be given either as a list of numbers (list can be of any length and list entries must be separated by commas) or as binary block data. When block data is transferred, 8 bytes are always interpreted as a floating-point number with double accu- racy (see :FORMat[:DATA] on page 298).

Range: Minimum level  to  Maximum level Default unit: dBm

Example:

LIST:SEL '/var/list3'

selects list3 for editing. The R&S SMB generates a new file automatically, if it does not exist yet.

LIST:POW 0dBm, 2dBm, 2dBm, 3dBm,..

specifies the level values in list3 . The number of level values must correspond to the number of frequency values. The previ- ous data is overwritten.

Manual operation:

See "Edit List Mode Data

