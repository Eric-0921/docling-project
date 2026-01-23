---
chapter_index: 2179
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<Deviation>

A five-digit value must always be set. Leading zeros, if any, must also be specified.

Range:

00000  to  10000 (ASCII coded decimal numbers), corresponding to 0 Hz to 100 kHz

Example:

STEReo:DIRect "MPX-DEV=00201"

Sets the MPX frequency deviation to 2.01 kHz.

Example:

STEReo: DIRECT ? "MPX-DEV"
  Response: "00201"

STEReo:DIRect "PI=<PI>"

STEReo:DIRect? "PI"

Sets or reads the RDS program identification (PI) code.

Setting parameters:

<PI>

Note: A four-digit value must always be set. Leading zeros, if any, must also be specified, otherwise the value will not be accepted.

Range:

0000  to  FFFF (ASCII coded hexadecimal num- bers)

Example:

STEReo:DIRect "PI=1234"

The program identification code to be transmitted is set to "1234".

Example:

STEReo: DIRECT? "PI"
  Response: "1234"

STEReo:DIRect "PIL=<State>"

STEReo:DIRect? "PIL"

(for documentation reasons only)

Activates/deactivates the pilot tone.

Use the SCPI command [:SOURce]:STEReo:PILot:STATe instead.

