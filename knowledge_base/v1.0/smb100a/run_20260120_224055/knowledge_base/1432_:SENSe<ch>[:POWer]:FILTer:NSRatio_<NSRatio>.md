---
chapter_index: 1432
title: ":SENSe<ch>[:POWer]:FILTer:NSRatio_<NSRatio>"
--- 

# :SENSe<ch>[:POWer]:FILTer:NSRatio_<NSRatio>

:SENSe<ch>[:POWer]:FILTer:NSRatio <NSRatio>

The command defines the noise content for fixed noise filter mode

( :SENSe<[1]

Parameters:

<NSRatio>

float

Range:

0.001  to  1

Increment:

0.001

*RST:

0.01

Example:

SENS1:FILT:TYPE NSR

selects fixed noise filter mode for the power sensor connected to the SENSOR connector.

SENS1:FILT:NSR 0.2

sets a noise content of 0.2.

Manual operation:

See "Noise Content" on page 176

