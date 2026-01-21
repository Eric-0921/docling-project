# :TRIGger<hw>:FSWeep[:IMMediate]
Immediately starts an RF frequency sweep cycle.

The command is only effective for sweep mode "Single" ( SOUR:SWE:FREQ:MODE AUTO in combination with TRIG:FSW:SOUR SING ).

The command corresponds to the manual control "Execute Single Sweep".

Example:

SWE:FREQ:MODE AUTO

sets the triggered sweep mode, i.e. a trigger is required to start the sweep.

TRIG:FSW:SOUR SING

sets the "Single" trigger mode, i.e. a trigger starts a single sweep.

TRIG:FSW

starts a single RF frequency sweep.

Usage:

Event

Manual operation:

See "Execute Single Sweep - Frequency Sweep" on page 183

