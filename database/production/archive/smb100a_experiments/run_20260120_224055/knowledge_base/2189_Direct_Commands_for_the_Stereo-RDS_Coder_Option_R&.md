---
chapter_index: 2189
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

0

no information concerning the character set table in the PS

1

table E.1 is used

2

table E.2 is used

3

table E.3 is used

STEReo:DIRect "PS-TABLE=2"

The information concerning the character set is transmitted in segment 0 of the PS in group 0A. To this end, segment 0 is transmitted repeatedly. At the first transmission segment 0 contains the information about the character set, at the second transmission segment 0 contains the first two characters of the PS.

STEReo:DIRect "PTY=<PTY>"

STEReo:DIRect? "PTY"

Sets or reads the program type (PTY).

