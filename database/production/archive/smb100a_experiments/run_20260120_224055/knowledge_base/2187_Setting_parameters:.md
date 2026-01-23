---
chapter_index: 2187
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<PS>

8 ASCII characters

Note: An eight-digit value must always be set. Blank spaces, if any, must also be entered, otherwise the value will not be accepted.

Special characters in the program service name are entered with a leading back slash (\) followed by the decimal code of the spezial character according to tabe E1 of CENELEC.

Example: STER:DIR "RT=02,0,test text with \217" 217 denotes the German ü.

Example:

STEReo:DIRect "PS=RDS Test"

Sets the program service name to be transmitted to "RDS Test".

Example:

STEReo:DIRect? "PS"

Response:

"RDS Test"

STEReo:DIRect "PS-TABLE=<Table>"

STEReo:DIRect? "PS-TABLE"

Selects the character set table tobe used for the display of the RDS program service (PS) name in the receiver.

The information concerning the character set is transmitted in segment 0 of the PS. Segment 0 is repeatedly transmtted if the value for PS-TABLE > 0. For PS-TABLE =0 no information concerning the character set is transmitted.

