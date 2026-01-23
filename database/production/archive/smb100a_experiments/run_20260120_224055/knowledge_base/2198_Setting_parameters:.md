---
chapter_index: 2198
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<RetranNumber>

<A/BFlag>

<RadioTextMsg>

Range:

0 | 1

If the A/B flag is set, the A/B bit in group 2A is toggled to signal that a new radio text message will be transmitted.)

max. 64 characters

Two texts of 64 characters each can be transmitted in a radio text message

Note: For group B, the length of a radio text is li ited to 32 characters. Special characters in the radio text are entered with a leading back slash (\) followed by the decimal code of the spezial character according to tabe E1 of CENELEC.

Example: STER:DIR "RT=02,0,test text with \217" 217 denotes the German ü.

Example:

STEReo:DIRect "RT=02,1,Test message 123"

The radio text message "Test message 123" is transmitted.

Example:

STEReo:DIRect? "RT"

Response:

"02,1,Test message 123"

STEReo:DIRect "SPS=<Time>,<PSN#1>,<PSN#2>,

Switching program service names (PSN). The program name automatically changed after the set time interval

00  to  15 (ASCII coded decimal numbers), number of retransmissions of radio text message

Operating Manual 1407.0806.32 ─ 23

482

R&S ® SMB100A

Remote Control Commands

