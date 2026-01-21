---
chapter_index: 2167
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

<Freq>

xxx.x

Sets the alternative frequencies as ASCII coded decimal num- bers.

If list <z> is not available, the response is ().

Note: For each Enhanced Other Network (EON), a maximum of five type B alternative frequency lists can be created, each list containing max. five frequencies, where <Freq#1> is Tuned Fre- quency (TF) and <Freq#2..5> are the Mapped Frequencies (MF). A minimum of two frequencies per EON is required.

Range:

87.6  to  107.9

Setting parameters:

<A>

N

new AF list

+

AF list to be added

Query parameters:

<z>

AF list to be read

Range:

1  to  5

Example:

STEReo:DIRect "EON-AFB=1000,N,97.4,98.3"

Creates a new type B alternative frequency list for the EON with PI=1000.

The list contains the alternative frequencies 97.4 MHz and 98.3 MHz.

Example:

STEReo:DIRect? "EON-AFB,1000,1"

Reads the first type B alternative frequency list of the EON with PI=1000.

Response:

"97.4,98.3"

STEReo:DIRect "EON-DEL=<PI>"

Enhanced Other Networks: deletes the complete EON with selected <PI>.

Parameters:

<PI>

Range:

0000  to  FFFF (ASCII coded hexadecimal num- bers)

Example:

STEReo:DIRect "EON-DEL=1000"

Deletes the EON with PI=1000.

Usage:

Setting only

STEReo:DIRect "EON-PI=<PI>" STEReo:DIRect? "EON-PI"

Enhanced Other Networks: creates a new EON or reads the list of the program identification (PI) codes of all EONs created so far.

Note: A maximum of eight EONs can be created.

Operating Manual 1407.0806.32 ─ 23

471

R&S ® SMB100A

Remote Control Commands

Parameters:

<PI>

Note: A four-digit value must always be set. Leading zeros, if any, must also be specified.

Range:

0000  to  FFFF (ASCII coded hexadecimal num- bers)

Example:

STEReo:DIRect "EON-PI=1000"

Creates a new EON with PI=1000.

Example:

STEReo:DIRect? "EON-PI"

Response:

"1000"

STEReo:DIRect "EON-PS=<PI>,<PS>" STEReo:DIRect? "EON-PS,<PI>"

Enhanced Other Networks: sets the program service (PS) name for the EON with the selected <PI>.

Parameters:

<PI>

Range:

0000  to  FFFF (ASCII coded hexadecimal num- bers)

Setting parameters:

<PS>

8 ASCII characters

Note: An eight-digit value must always be set. Blank spaces, if any, must also be entered, otherwise the value will not be accep- ted.

Example:

STEReo:DIRect "EON-PS=1000,Test 123"

Sets the program service name for the EON with PI=1000 to "Test 123".

Example:

STEReo:DIRect? "EON-PS,1000"

Reads the program service name of the EON with PI=1000. Response: "Test 123"

STEReo:DIRect "EON-PTY=<PI>,<PTY>"

STEReo:DIRect? "EON-PTY,<PI>"

Enhanced Other Networks: sets the program type (PTY) for the EON with the selected <PI>.

Parameters:

<PI>

Range:

0000  to  FFFF (ASCII coded hexadecimal num- bers)

Setting parameters:

<PTY>

Range:

00  to  31 (ASCII coded decimal numbers)

Example:

STEReo:DIRect "EON-PTY=1000,10"

Sets the program type for the EON with PI=1000 to "10".

