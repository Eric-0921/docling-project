---
chapter_index: 2200
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<Time>

Time interval in seconds

Range:

00  to  59 s

Example:

STEReo:DIRect "SPS=05,TEST0123,TEST4567"

The program service names "TEST0123" and "TEST4567" are alternately transmitted at an interval of 5 seconds.

Example:

STEReo:DIRect? 'SPS'

Queries the program service names

Response:

"05,TEST0123,TEST4567"

STEReo:DIRect "SRC=<SigSource>"

STEReo:DIRect? "SRC"

(for documentation reasons only)

Selects the signal source.

Use the SCPI command [:SOURce]:STEReo:SOURce instead.

