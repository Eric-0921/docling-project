# 6.13.16 SOURce:SWEep Subsystem
The SOURce: subsystem contains the commands for configuring RF sweep signals.

![Picture](#/pictures/332)

The keyword [:FREQuency] can be ommitted, then the commands are SCPIcompliant.

To activate a RF sweep mode, use the following commands:

-RF frequency sweep: SOURce:FREQuency:MODE SWEep ( SOURce:FREQuency:MODE CW (off))

-RF level sweep: SOURce:POWer:MODE SWEep ( SOURce:POWer:MODE CW (off))

All sweeps, including the LF sweep, can be set independently from each other.

This example shows how to set up a frequency sweep.

Set the sweep range. SOUR:FREQ:CENT 200 MHz

Operating Manual 1407.0806.32 ─ 23

421

R&S ® SMB100A

Remote Control Commands

![Picture](#/pictures/333)

SOUR:FREQ:SPAN 300 MHz

Select linear or logarithmic spacing.

Set the step width and dwell time.

Select the trigger mode.

SOUR: SWE: FREQ: SPAC  LIN

SOUR::SWE::FREQ::STEP:LIN	20	MHZ
      SOUR::SWE::FREQ::DWEL	12	ms

TRIG:FSW:SOUR SING

Select the sweep mode and activate the sweep.

Trigger the sweep.

SOUR:SWE:FREQ:MODE AUTO

SOUR:FREQ:MODE SWE

SOURce:SWE:FREQ:EXEC

It is recommended that you switch off the "Start/Stop Display Update" for optimum sweep performance, especially with short dwell times ( SYST:DISP:UPD OFF ).

| [:SOURce<hw>]:SWEep[:FREQuency]:DWELl..................................................................422        |
|-------------------------------------------------------------------------------------------------------------------|
| [:SOURce<hw>]:SWEep[:FREQuency]:EXECute.............................................................. 423         |
| [:SOURce<hw>]:SWEep[:FREQuency]:LFConnector.........................................................423           |
| [:SOURce<hw>]:SWEep[:FREQuency]:MODE..................................................................424         |
| [:SOURce<hw>]:SWEep[:FREQuency]:OVOLtage:STARt.................................................. 424              |
| [:SOURce<hw>]:SWEep[:FREQuency]:OVOLtage:STOP...................................................425               |
| [:SOURce<hw>]:SWEep[:FREQuency]:POINts................................................................. 425       |
| [:SOURce<hw>]:SWEep[:FREQuency]:RETRace..............................................................426          |
| [:SOURce<hw>]:SWEep[:FREQuency]:RUNNing?............................................................ 426          |
| [:SOURce<hw>]:SWEep[:FREQuency]:SHAPe.................................................................426         |
| [:SOURce<hw>]:SWEep[:FREQuency]:SPACing...............................................................427         |
| [:SOURce<hw>]:SWEep[:FREQuency]:STEP[:LINear].......................................................427           |
| [:SOURce<hw>]:SWEep[:FREQuency]:STEP:LOGarithmic................................................428               |
| [:SOURce<hw>]:SWEep:POWer:DWELl...........................................................................429     |
| [:SOURce<hw>]:SWEep:POWer:EXECute....................................................................... 429      |
| [:SOURce<hw>]:SWEep:POWer:MODE...........................................................................430      |
| [:SOURce<hw>]:SWEep:POWer:POINts..........................................................................430     |
| [:SOURce<hw>]:SWEep:POWer:RETRace.......................................................................431       |
| [:SOURce<hw>]:SWEep:POWer:RUNNing?.....................................................................431        |
| [:SOURce<hw>]:SWEep:POWer:SHAPe..........................................................................431      |
| [:SOURce<hw>]:SWEep:POWer:SPACing:MODE?........................................................... 432            |
| [:SOURce<hw>]:SWEep:POWer:STEP[:LOGarithmic]....................................................... 432           |
| [:SOURce<hw>]:SWEep:RESet[:ALL].............................................................................. 433 |
[:SOURce<hw>]:SWEep[:FREQuency]:DWELl <Dwell>

Sets the time taken for each frequency step of the sweep.

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

422

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

The keyword [ :FREQuency ] can be omitted (see example). The command is then SCPI-compliant.

Tip: It is recommended to switch off the "Display Update" for optimum sweep performance especially with short dwell times ( SYSTem:DISPlay:UPDate OFF ).

