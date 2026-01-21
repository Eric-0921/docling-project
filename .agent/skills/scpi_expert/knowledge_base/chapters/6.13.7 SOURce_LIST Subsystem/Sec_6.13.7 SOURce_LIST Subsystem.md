# 6.13.7 SOURce:LIST Subsystem
This subsystem contains the commands for the List mode of the instrument.

The following settings are required to operate the instrument in List mode:

Create a list.

If a list which does not exist is selected with the :LIST:SEL command, an empty list with the name of the selected list is created.

SOUR1:LIST:SEL "New_list"


Fill the list with values.

All list components must be of the same length. This does not apply to components of length 1. This is interpreted as if the component has the same length as the other components and as if all values are the same as the first value.

SOUR1:LIST:FREQ 100  MHz,  110  MHz,  120  MHz...
      SOUR1:LIST:POW 2dBm,  -1dBm,  0dBm...


Select a list.

If a new empty file has been created with the :LIST:SEL command, this file is selected, otherwise an existing list must be selected before the List mode is activated.

SOUR1:LIST:SEL "Old_list"


Set the dwell time.

The dwell time determines the duration of the individual list steps.

SOUR1 : LIST: DWEL  3ms


Set the List mode.

The List mode determines the way in which the list is processed. In the example the list is processed once only or repeatedly depending on the trigger setting. SOUR1:LIST:MODE AUTO

Determine the trigger.

Operating Manual 1407.0806.32 ─ 23

364

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

![Picture](#/pictures/330)

In the example each trigger causes the list to be processed once from beginning to end.

SOUR:LIST:TRIG:SOUR SING

Activate the List mode. SOUR1:FREQ:MODE LIST

Trigger the list (depending on the mode).

SOUR1:LIST:TRIG:EXEC

Deactivate the List mode.

SOUR1:FREQ:MODE CW

SCPI refers to the individual lists as segments.

| [:SOURce<hw>]:LIST:CATalog?.......................................................................................365   |
|-------------------------------------------------------------------------------------------------------------------------|
| [:SOURce<hw>]:LIST:DELete..........................................................................................366  |
| [:SOURce<hw>]:LIST:DELete:ALL...................................................................................366     |
| [:SOURce<hw>]:LIST:DEXChange:AFILe:CATalog?.......................................................... 367               |
| [:SOURce<hw>]:LIST:DEXChange:AFILe:EXTension.........................................................367                |
| [:SOURce<hw>]:LIST:DEXChange:AFILe:SELect..............................................................368              |
| [:SOURce<hw>]:LIST:DEXChange:AFILe:SEParator:COLumn........................................... 368                      |
| [:SOURce<hw>]:LIST:DEXChange:AFILe:SEParator:DECimal........................................... 369                     |
| [:SOURce<hw>]:LIST:DEXChange:EXECute.................................................................... 369            |
| [:SOURce<hw>]:LIST:DEXChange:MODE........................................................................370            |
| [:SOURce<hw>]:LIST:DEXChange:SELect....................................................................... 370          |
| [:SOURce<hw>]:LIST:DWELl.......................................................................................... 370  |
| [:SOURce<hw>]:LIST:FREE?..........................................................................................371   |
| [:SOURce<hw>]:LIST:FREQuency...................................................................................371      |
| [:SOURce<hw>]:LIST:FREQuency:POINts?......................................................................372           |
| [:SOURce<hw>]:LIST:INDex............................................................................................372 |
| [:SOURce<hw>]:LIST:INDex:STARt................................................................................. 372     |
| [:SOURce<hw>]:LIST:INDex:STOP..................................................................................373      |
| [:SOURce<hw>]:LIST:LEARn.......................................................................................... 373  |
| [:SOURce<hw>]:LIST:MODE...........................................................................................374   |
| [:SOURce<hw>]:LIST:POWer..........................................................................................374   |
| [:SOURce<hw>]:LIST:POWer:POINts?.............................................................................374        |
| [:SOURce<hw>]:LIST:RESet...........................................................................................375  |
| [:SOURce<hw>]:LIST:SELect..........................................................................................375  |
| [:SOURce<hw>]:LIST:TRIGger:EXECute..........................................................................375         |
| [:SOURce<hw>]:LIST:TRIGger:SOURce.......................................................................... 376         |
