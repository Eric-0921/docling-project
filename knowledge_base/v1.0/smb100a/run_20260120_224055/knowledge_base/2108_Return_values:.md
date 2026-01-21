---
chapter_index: 2108
title: "Return_values:"
--- 

# Return_values:

Return values:

<Result>

0 | 1 | RUNning | STOPped

0

Success

1

Fail

*RST:

STOPped

Example:

TEST:ALL:STAR

Starts the self-test

TEST:ALL:RES?

Usage:

Query only

Manual operation:

See "Start Selftest" on page 497

:TEST<hw>:DIRect <HW_assembly>,<subadress>,<hex data string> :TEST<hw>:DIRect? <HW_assembly>,<subadress>

The respective hardware assembly responds directly to the command; any safety mechanisms are bypassed. This function is only available via remote control.

Example:

TEST:DIR 'SSYN',0,#H12345678

TEST:DIR? 'SSYN',0

Response:

#H12345678

