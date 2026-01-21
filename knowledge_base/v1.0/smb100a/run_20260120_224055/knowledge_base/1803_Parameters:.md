---
chapter_index: 1803
title: "Parameters:"
--- 

# Parameters:

Parameters:

<OnTime>

Ontime#1{, Ontime#2,

The data can be given either as a list of numbers (list can be of any length and list entries must be separated by commas) or as binary block data.

When block data is transferred, 8 (4) bytes are always interpre- ted as a floating-point number with double accuracy (see the command FORMat:DATA ).

The maximum length is 2047 values.

Example:

MMEM:CDIR '/var/user/Lists'

selects the directory for the pulse train files.

PULM:TRA:SEL 'P_INCR'

selects P_INCR for editing. P_INCR is created if it does not yet exist.

PULM:TRA:ONT 10ns,30ns,40ns,

specifies the on-time values in P_INCR . If the list already con- tains data, it is overwritten.

Options:

R&S SMB-K27 (Pulse Train)

Manual operation:

See "Edit Pulse Train Data" on page 237

