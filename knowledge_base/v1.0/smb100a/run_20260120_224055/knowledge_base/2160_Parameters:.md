---
chapter_index: 2160
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Code>

A | B | C | D | E | F

Example:

STEReo:DIRect "BK=E"

The ARI area identification is set to "E".

Example:

STEReo:DIRect? "BK"

Response:

"E"

STEReo:DIRect "CT= <Hour>:<Min>:<Sec>,<Day>.<Month>.<Year>" STEReo:DIRect? "CT"

Sets and activates transmission of the real-time clock.

Note: The CT data is transmitted in group 4A. Setting the real-time clock (CT command) automatically adds group 4A to the group sequence. Group 4A must not be manually added to, or removed from, the group sequence. To remove group 4A from the group sequence, use the command "CT=off" .

