---
chapter_index: 2182
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<Deviation>

Note: A four-digit value must always be set. Leading zeros, if any, must also be specified.

Range:

0000  to  1000 (ASCII coded decimal numbers), corresponding to 0 Hz to 10 kHz

Example:

STEReo:DIRect "PIL-DEV=1000"

Sets the frequency deviation of the pilot tone to 10 kHz.

Example:

STEReo:DIRect? "PIL-DEV"

Response:

"1000"

STEReo:DIRect "PIL-PH=<Phase>" STEReo:DIRect? "PIL-PH"

(for documentation reasons only)

Sets the pilot tone phase.

Use the SCPI command [:SOURce]:STEReo:PILot:PHASe instead.

