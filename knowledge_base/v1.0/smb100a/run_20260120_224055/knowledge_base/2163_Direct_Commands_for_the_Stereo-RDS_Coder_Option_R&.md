---
chapter_index: 2163
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

STEReo:DIRect "DI=<x>"

STEReo:DIRect?

"DI"

Sets or reads the decoder information (DI).

With this command, the current decoder operating mode (mono, stereo, etc) can be detected and, if necessary, changed.

Parameters:

<x>

Range:

0  to  F (ASCII coded hexadecimal numbers)

Example:

STEReo:DIRect "DI=4"

The decoder information is set to "4".

Example:

STEReo:DIRect? "DI"

Response:

"4"

STEReo:DIRect "DS=<x>" STEReo:DIRect? "DS"

(for documentation reasons only)

Selects/activates a storage area in the Stereo/RDS Coder.

Upon activation, the settings stored in the selected area can be loaded.

Use SCPI command [:SOURce]:STEReo:RDS:DATaset instead.

Parameters:

<x>

Range:

1  to  5

Example:

STEReo:DIRect "DS=2"

Storage area 2 is activated.

Example:

STEReo:DIRect? "DS"

Response:

"2"

STEReo:DIRect "EON-AFA= <PI>,<A>,<Freq#1>,<Freq#2>,

Enhanced Other Networks: defines type A alternative frequencies for the EON with the selected PI.

