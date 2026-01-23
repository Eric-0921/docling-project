---
chapter_index: 2177
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<Flag>

M | S

Example:

STEReo:DIRect "MS=M"

The music/speech flag is set to "M". This signals that music is currently transmitted.

Example:

STEReo:DIRect? "MS"

Response:

"M"

STEReo:DIRect "MPX-DEV=<Deviation>" STEReo:DIRect? "MPX-DEV"

(for documentation reasons only)

Sets the MPX frequency deviation (max. deviation).

Use the SCPI command [:SOURce]:STEReo[:DEViation] instead.

Operating Manual 1407.0806.32 ─ 23

476

R&S ® SMB100A

Remote Control Commands

