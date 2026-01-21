---
chapter_index: 2169
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

Example:

STEReo:DIRect? "EON-PTY,1000"

Reads the program type of the EON with PI=1000.

Response: "10"

STEReo:DIRect "EON-TA=<PI>,<TA>"

STEReo:DIRect? "EON-TA,<PI>"

Enhanced Other Networks: sets the TA flag for the EON with the selected <PI>.

Parameters:

<PI>

Range:

0000  to  FFFF (ASCII coded hexadecimal num-

bers)

Setting parameters:

<TA>

0 | 1

Example:

STEReo:DIRect "EON-TA=1000,1"

Sets the TA flag for the EON with PI=1000 to "1".

Example:

STEReo:DIRect? "EON-TA,1000"

Reads the TA flag of the EON with PI=1000.

Response:

"1"

STEReo:DIRect "EON-TP=<PI>,<TP>"

STEReo:DIRect? "EON-TP,<PI>"

Enhanced Other Networks: sets the TP flag for the EON with the selected <PI>.

Parameters:

<PI>

Range:

0000  to  FFFF (ASCII coded hexadecimal num- bers)

Setting parameters:

<TP>

0 | 1

Example:

STEReo:DIRect "EON-TP=1000,1"

Sets the TP flag for the EON with PI=1000 to "1".

Example:

STEReo:DIRect? "EON-TP,1000"

Reads the TP flag of the EON with PI=1000.

Response:

"1"

STEReo:DIRect "GS=<Group#1>,<Group#2>,

Sets or reads the group sequence.

Note: Only group A or group B data may be sent at a time. Only groups that contain data are transmitted. The groups 4A, 14B and 15B are automatically added to the group sequence and must not be added or removed manually.

Setting parameters:

<Group>

0A,1A,2A, … to 15B

Operating Manual 1407.0806.32 ─ 23

473

R&S ® SMB100A

Remote Control Commands

