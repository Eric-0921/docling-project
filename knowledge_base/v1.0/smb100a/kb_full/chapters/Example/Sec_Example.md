# Example
The following example shows how to set an LF sweep.

Set the sweep range.

Select linear or logarithmic sweep spacing.

LFOutput : FREQuency:START  4  kHz
      LFOutput : FREQuency:STOP 10  kHz

LFOutput:SWEep[:FREQuency]:SPACing LIN

Set the step width and dwell time.

Determine the sweep mode.

LFOutput::SWEp [ :FREQquency] :STEP [ :LINEar]  100  Hz
         LFOutput::SWEp [ :FREQquency] :DWELL  20  ms


LFOutput:SWEep:MODE AUTO

Determine the trigger.

Operating Manual 1407.0806.32 ─ 23

354

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

6.

TRIGger0:SOURce SINGle

Activate the sweep. LFOutput:FREQuency:MODE SWEep

Trigger the sweep (depending on the mode). LFOutput:SWEep:EXECute

| [:SOURce]:LFOutput<ch>:FREQuency.............................................................................355         |
|--------------------------------------------------------------------------------------------------------------------------|
| [:SOURce<hw>]:LFOutput:FREQuency:MANual............................................................... 356               |
| [:SOURce<hw>]:LFOutput:FREQuency:MODE................................................................. 356               |
| [:SOURce<hw>]:LFOutput:FREQuency:STARt..................................................................357              |
| [:SOURce<hw>]:LFOutput:FREQuency:STOP.................................................................. 357              |
| [:SOURce]:LFOutput[:STATe].......................................................................................... 357 |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:DWELl................................................... 358                    |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:EXECute................................................358                      |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:MODE....................................................358                     |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:POINts...................................................359                    |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:RETRace............................................... 360                      |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:RUNNing?..............................................360                       |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:SHAPe...................................................361                     |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:SPACing................................................ 361                     |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:STEP[:LINear]........................................ 361                       |
| [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:STEP:LOGarithmic..................................362                           |
| [:SOURce]:LFOutput:SHAPe...........................................................................................363   |
| [:SOURce]:LFOutput:SIMPedance...................................................................................363      |
| [:SOURce]:LFOutput:VOLTage........................................................................................364    |
