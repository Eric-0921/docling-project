---
chapter_index: 2153
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

Query parameters:

<z>

AF list to be read

Range:

1  to  5

Example:

STEReo:DIRect "AF=N,97.4,98.3"

Defines an alternative frequency list, the alternative frequencies 97.4 and 98.3 are inserted.

Example:

STEReo:DIRect? "AF1"

Reads the first alternative frequency list.

Response:

"97.4,98.3"

Example:

STEReo:DIRect "AF=N"

Deletes all frequency lists.

STEReo:DIRect "ARI=<State>" STEReo:DIRect? "ARI"

(for documentation reasons only)

Activates ARI signal transmission.

Use SCPI command [:SOURce]:STEReo:ARI:STATe instead.

Setting parameters:

<State>

0 | 1

Example:

STEReo:DIRect "ARI=0"

Deactivates ARI signal transmission.

Example:

STEReo:DIRect? "ARI"

Response:

"0"

STEReo:DIRect "ARI-DEV=<Deviation>" STEReo:DIRect? "ARI-DEV"

(for documentation reasons only)

Sets the frequency deviation of the ARI signal (max. deviation).

Use SCPI command [:SOURce]:STEReo:ARI[:DEViation] instead.

