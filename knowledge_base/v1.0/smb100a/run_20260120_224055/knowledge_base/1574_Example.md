---
chapter_index: 1574
title: "Example"
--- 

# Example

Example

The following example shows how to set an LF sweep.

Set the sweep range.

LFOutput : FREQuency:START  4  kHz
      LFOutput : FREQuency:STOP 10  kHz

Select linear or logarithmic sweep spacing.

LFOutput:SWEep[:FREQuency]:SPACing LIN

Set the step width and dwell time.

LFOutput::SWEp [ :FREQquency] :STEP [ :LINEar]  100  Hz
         LFOutput::SWEp [ :FREQquency] :DWELL  20  ms

Determine the sweep mode.

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

