# set sweep mode "Step".
SOUR:FREQ:MODE SWE

activate sweep mode, the frequency is set to "Start Freq".

SOUR:FREQ:MAN UP

set the frequency to the next higher sweep frequency.

SOUR:FREQ:MAN DOWN

set the frequency to the next lower sweep frequency.

Generates a single sweep cycle when an a external trigger event occurs.

The sweep steps within the cycle are performed automatically, controlled by the dwell time. If one cycle is completed, the instrument waits for the next trigger event.

To trigger the sweep, apply an external trigger signal.

Refer to the description of the rear panel for information on the connectors for external trigger signal input (see Chapter 3.2.2, "Rear Panel Tour", on page 54).

