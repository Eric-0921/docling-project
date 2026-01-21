---
chapter_index: 2183
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<Phase>

Note: A two-digit value must always be set with a sign ("+" or "-") in front of it. Leading zeros, if any, must also be specified.

Range:

-5.0  to  +5.0 (ASCII coded decimal numbers), cor- responding to ±5.0

Example:

STEReo:DIRect "PIL-PH=-33"

The pilot tone phase is set to 3.3

Example:

STEReo:DIRect? "PIL-PH"

Response:

"-33"

STEReo:DIRect "PRE=<Preemphasis>" STEReo:DIRect? "PRE"

(for documentation reasons only)

Sets one of various preemphasis options.

Use the SCPI commands [:SOURce]:STEReo:AUDio:PREemphasis:STATe and [:SOURce]:STEReo:AUDio:PREemphasis instead.

