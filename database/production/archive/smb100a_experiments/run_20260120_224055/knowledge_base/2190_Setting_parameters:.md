---
chapter_index: 2190
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<PTY>

Note: A two-digit value must always be set. A leading zero, if any, must also be specified.

Range:

00  to  31 (ASCII coded decimal numbers)

Example:

STEReo:DIRect "PTY=08"

Sets the program type to be transmitted to "08".

Example:

STEReo:DIRect? "PTY"

Response:

"08"

STEReo:DIRect "PTYN=<PTYN>"

STEReo:DIRect? "PTYN"

Sets or reads the RDS program type (PTY) name.

