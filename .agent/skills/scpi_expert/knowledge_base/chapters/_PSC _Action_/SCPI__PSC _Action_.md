# *PSC <Action>
Power on status clear

Determines whether the contents of the ENABle registers are preserved or reset when the instrument is switched on. Thus a service request can be triggered when the instrument is switched on, if the status registers ESE and SRE are suitably configured. The query reads out the contents of the "power-on-status-clear" flag.


## Parameters:
<Action>

0 | 1

0

The contents of the status registers are preserved.

1

Resets the status registers.

