---
chapter_index: 2194
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<Phase>

Range:

000  to  359 (ASCII coded decimal numbers)

Example:

STEReo:DIRect "RDS-PH=100"

The RDS phase is set to 100.

Example:

STEReo:DIRect? "RDS-PH"

Response:

"100"

STEReo:DIRect "RDS-DEV=<Deviation>" STEReo:DIRect? "RDS-DEV"

(for documentation reasons only)

Sets the RDS frequency deviation (max. deviation).

Use the SCPI command [:SOURce]:STEReo:RDS[:DEViation] instead.

