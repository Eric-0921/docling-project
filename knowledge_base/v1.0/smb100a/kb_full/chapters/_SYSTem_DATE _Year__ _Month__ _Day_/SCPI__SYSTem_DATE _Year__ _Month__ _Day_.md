# :SYSTem:DATE <Year>, <Month>, <Day>
Queries or sets the date for the instrument-internal calendar.

This parameter is protected, in order to prevent accidental changes.

It can be accessed with protection level 1, see :SYSTem:PROTect<ch>[:STATe] on page 452.


## Parameters:
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


## Parameters:
<Hour>

0...23,0...59,0...59

Range:

0  to  23

<Minute>

integer

Range:

0  to  59

Operating Manual 1407.0806.32 ─ 23

454

R&S ® SMB100A

Remote Control Commands

string

