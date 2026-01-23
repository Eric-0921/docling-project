---
chapter_index: 2192
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

Example:

STEReo:DIRect? "PTYN"

Response: "Football"

Example:

STEReo:DIRect "PTYN="

Transmission of PTYN in group 10A is stopped, even if group 10A is contained in the group sequence.

STEReo:DIRect "RDS=<State>" STEReo:DIRect? "RDS"

(for documentation reasons only)

Switches RDS on or off.

Use the SCPI command [:SOURce]:STEReo:RDS:STATe instead.

