---
chapter_index: 1428
title: ":SENSe<ch>[:POWer]:FILTer:LENGth:AUTO?"
--- 

# :SENSe<ch>[:POWer]:FILTer:LENGth:AUTO?

:SENSe<ch>[:POWer]:FILTer:LENGth:AUTO?

The command queries the current filter length for auto filter mode

( :SENSe<[1]

Return values:

<Auto>

float

Range:

1  to  65536

Example:

SENS1:FILT:TYPE AUTO

selects auto filter mode for the power sensor connected to the SENSOR connector.

SENS1:FILT:LENG:AUTO?

queries the automatically set filter length.

Response: 1024

Usage:

Query only

Manual operation:

See "Filter Length" on page 176

