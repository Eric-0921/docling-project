---
chapter_index: 2089
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Year>

<year>,<month>,<day>

<Month>

integer

Range:

1  to  12

<Day>

integer

Range:

1  to  31

Example:

SYST:DATE?

Response:

"2011,05,01"

it is the 1st of May, 2011.

Manual operation:

See "Date" on page 492

:SYSTem:TIME <Hour>, <Minute>, <Second>

Queries or sets the time for the instrument-internal clock.

The parameter is protected, in order to prevent accidental changes.

It can be accessed with protection level 1, see :SYSTem:PROTect<ch>[:STATe] on page 452.

