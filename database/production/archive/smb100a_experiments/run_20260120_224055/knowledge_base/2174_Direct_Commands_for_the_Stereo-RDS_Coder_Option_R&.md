---
chapter_index: 2174
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

<BitMaskBlc>

<BitMaskBlcA>,<BitMaskBlcB>,<BitMaskBlcC>,<BitMaskBlcD>

Hexadecimal bit mask for blocks A, B, C and D of the RDS groups. For each block, 26 bits (16 data bits and 10 CRC bits) have to be entered in hexadecimal code.

Range:

0000000  to  3FFFFFFF

Example:

STEReo:DIRect

"MASK=09,01,0000001,0000000,0000000,0000000"

In nine RDS groups, the least significant bit of the CRC code of block A is inverted, i.e. an errored bit is sent. After each errored group, one error-free group is inserted. After transmission of the complete sequence, MASK_STATE is set to "0".

With the command MASK_STATE=1 , the above sequence (9 errored groups with one error-free group inserted after each errored group) is retransmitted once.

Then, MASK_STATE is again set to "0".

Example:

STEReo:DIRect? "MASK"

Response:

"09,01,0000001,0000000,0000000,0000000"

STEReo:DIRect

"MASK_STATE=<State>"

STEReo:DIRect? "MASK_STATE"

Switches on or off the transmission of defined bit errors in the RDS data stream.

Setting parameters:

<State>

0 | 1

Example:

STEReo:DIRect "MASK_STATE=1"

With the command MASK_STATE=1 , a sequence of errored groups as defined by the MASK command is retransmitted once if the number of groups to be masked is other than zero. Then, MASK_STATE is automatically set to "0".

If the number of groups to be masked is equal to zero in the MASK command (which means continuous error transmission), the masking function can be switched off with MASK_STATE=0 .

Example:

STEReo:DIRect? "MASK_STATE"

Response:

"1"

The MASK_STATE query provides information as to whether the RDS data stream is linked to an error mask.

STEReo:DIRect "MODE=<EMODE>" STEReo:DIRect? "MODE"

(for documentation reasons only)

Sets one of various transmit modes.

Operating Manual 1407.0806.32 ─ 23

475

R&S ® SMB100A

Remote Control Commands

