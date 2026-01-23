---
chapter_index: 1594
title: "MANual"
--- 

# MANual

MANual

Performs a single sweep step when a manual trigger event occurs.

The trigger system is not active. You can trigger each frequency step of the sweep individually with the command [:

SOURce<hw>]:LFOutput:FREQuency:MANual . In manual mode, use the rotary knob for switching to the next step.

With each step, the frequency increases by the value specified with the command [:SOURce<hw>]:LFOutput:SWEep[:

FREQuency]:STEP[:LINear]

or

[:SOURce<hw>]:

LFOutput:SWEep[:FREQuency]:STEP:LOGarithmic

,

respectively. A frequency value, entered with [:SOURce<hw>]: LFOutput:FREQuency:MANual takes no effect.

With manual control, the frequency increases or decreases (depending on the direction of the rotary encoder) by the value specified under SOUR:LFO:SWE:FREQ:STEP:LIN (linear spacing) or

