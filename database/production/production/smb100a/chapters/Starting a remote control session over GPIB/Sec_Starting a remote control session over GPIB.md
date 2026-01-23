# Starting a remote control session over GPIB
As a prerequisite, the GPIB address of the instrument, which is factory-set to 28, must not have been changed.

Connect instrument and controller using GPIB cable and switch them on.

Execute following commands on the controller:

Open port to the instrument

CALL IBFIND("DEV1", generator%) b) Inform controller about instrument address CALL IBPAD(generator%, 28) c) Reset instrument CALL IBWRT(generator%, "*RST;*CLS") d) Set instrument to new address CALL IBWRT(generator%, "SYST:COMM:GPIB:ADDR 18") e) Inform controller about new address CALL IBPAD(generator%, 18)

The GPIB address of the instrument is changed.

To return to manual operation sent CALL IBLOC (generator%) or press the [LOCAL] key at the front panel.

