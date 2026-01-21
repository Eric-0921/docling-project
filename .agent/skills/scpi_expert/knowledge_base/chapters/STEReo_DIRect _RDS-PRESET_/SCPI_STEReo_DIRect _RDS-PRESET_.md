# STEReo:DIRect "RDS-PRESET"
All RDS specific parameters are deleted or set to a default values.

Example:

STEReo:DIRect "RDS-PRESET"

Sets all RDS parameter to their preset values

Usage:

Event

STEReo:DIRect "RT=<RetranNumber>,<A/

BFlag>,<RadioTextMsg#1>,<RadioTextMsg#2>"

STEReo:DIRect? "RT"

Radio text


## Setting parameters:
<RetranNumber>

<A/BFlag>

<RadioTextMsg>

Range:

0 | 1

If the A/B flag is set, the A/B bit in group 2A is toggled to signal that a new radio text message will be transmitted.)

max. 64 characters

Two texts of 64 characters each can be transmitted in a radio text message

Note: For group B, the length of a radio text is li ited to 32 characters. Special characters in the radio text are entered with a leading back slash (\) followed by the decimal code of the spezial character according to tabe E1 of CENELEC.

Example: STER:DIR "RT=02,0,test text with \217" 217 denotes the German ü.

Example:

STEReo:DIRect "RT=02,1,Test message 123"

The radio text message "Test message 123" is transmitted.

Example:

STEReo:DIRect? "RT"

Response:

"02,1,Test message 123"

STEReo:DIRect "SPS=<Time>,<PSN#1>,<PSN#2>,...<PSN#20>" STEReo:DIRect? "SPS"

Switching program service names (PSN). The program name automatically changed after the set time interval

00  to  15 (ASCII coded decimal numbers), number of retransmissions of radio text message

Operating Manual 1407.0806.32 ─ 23

482

R&S ® SMB100A

Remote Control Commands


## Parameters:
<PSN>

8 ASCII characters

Max. 20 program service names of eight characters each can be entered.

Note: The program service names have to be entered as 8-digit texts. Blank spaces, if any, must also be entered, otherwise the value will not be accepted.

STEReo:DIRect 'SPS=0' stopps the transmission of the scrolling PS beendet and starts the transmission of the standard PS.


## Setting parameters:
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


## Setting parameters:
<SigSource>

0 | 1 | 2 | 3

0

Off

1

external analog (via L and R inputs)

2

external digital

3

internal with LF generator

Example:

STEReo:DIRect "SRC=1"

The external analog L and R inputs are selected as source.

Example:

STEReo:DIRect? "SRC"

Response:

"1"

