---
chapter_index: 2165
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

<Freq>

xxx.x

Sets the alternative frequencies as ASCII coded decimal num- bers.

If list <z> is not available, the response is ().

Note: For each Enhanced Other Network (EON), a maximum of five type A alternative frequency lists can be created.

Range:

87.6  to  107.9

Setting parameters:

<A>

N

new AF list

+

AF list to be added

Query parameters:

<z>

AF list to be read

Range:

1  to  5

Example:

STEReo:DIRect "EON-AFA=1000,N,97.4,98.3"

Creates a new type A alternative frequency list for the EON with PI=1000.

The new list contains the alternative frequencies 97.4 MHz and 98.3 MHz.

Example:

STEReo:DIRect? "EON-AFA,1000,1"

Reads the first type A alternative frequency list of the EON with PI=1000.

Response:

"97.4,98.3"

STEReo:DIRect "EON-AFB= <PI>,<A>,<Freq#1>,<Freq#2>,

Enhanced Other Networks: defines type B alternative frequencies for the EON with the selected PI.

