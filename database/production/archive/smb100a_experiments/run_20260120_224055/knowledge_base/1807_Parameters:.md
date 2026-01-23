---
chapter_index: 1807
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Repetition>

Repetition#1{, Repetition#2,

Range:

0

Example:

MMEM:CDIR '/var/user/Lists'

selects the directory for the pulse train files.

PULM:TRA:SEL 'P_INCR'

selects P_INCR for editing. P_INCR is created if it does not yet exist.

PULM:TRA:ONT 10ns,30ns,40ns,

specifies the ontime values in P_INCR . If the list already con- tains data, it is overwritten.

PULM:TRA:OFFT 10ns,30ns,40ns,

specifies the offtime values in P_INCR . If the list already con- tains data, it is overwritten.

PULM:TRA:REP 1,8,3,

specifies the number of repetitions for each value pair.

Options:

R&S SMB-K27 (Pulse Train)

Manual operation:

See "Edit Pulse Train Data" on page 237

