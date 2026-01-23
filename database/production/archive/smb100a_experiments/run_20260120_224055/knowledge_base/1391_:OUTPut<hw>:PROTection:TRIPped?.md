---
chapter_index: 1391
title: ":OUTPut<hw>:PROTection:TRIPped?"
--- 

# :OUTPut<hw>:PROTection:TRIPped?

:OUTPut<hw>:PROTection:TRIPped?

Queries the state of the protective circuit.

OUTPut Subsystem

Operating Manual 1407.0806.32 ─ 23

316

R&S ® SMB100A

Remote Control Commands

Return values:

<Tripped>

0 | 1 | OFF | ON

*RST:

0

Example:

OUTP:PROT:TRIP

Queries the state of the protective circuit for RF output A.

Response: 0

The protective circuit has not tripped.

Response: 1

The protective circuit has tripped.

Usage:

Query only

Manual operation:

See "Overload" on page 167

