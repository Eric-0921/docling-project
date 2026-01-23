---
chapter_index: 1511
title: "[:SOURce<hw>]:CORRection[:STATe]_<State>"
--- 

# [:SOURce<hw>]:CORRection[:STATe]_<State>

[:SOURce<hw>]:CORRection[:STATe] <State>

Activates/deactivates level correction. Level correction is performed using the table which has been selected with the command [:SOURce<hw>]:CORRection:CSET[: SELect] .

Parameters:

<State>

0 | 1 | OFF | ON

*RST:

0

Example:

SOUR:CORR:CSET '/var/user/ucor1'

selects the table ucor1 .

SOUR:CORR ON

activates user correction.

Manual operation:

See "State - User Correction" on page 160

