---
chapter_index: 2170
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

Example:

STEReo:DIRect "GS=0A,1B,10A,15A"

The groups 0A,1B,10A,15A are transmitted.

Example:

STEReo:DIRect? "GS"

Response:

"0A,1B,10A,15A"

STEReo:DIRect "IMP=<x>" STEReo:DIRect? "IMP"

(for documentation reasons only)

Sets external L, R impedances.

Use the SCPI command [:SOURce]:STEReo:EXTernal:IMPedance instead.

