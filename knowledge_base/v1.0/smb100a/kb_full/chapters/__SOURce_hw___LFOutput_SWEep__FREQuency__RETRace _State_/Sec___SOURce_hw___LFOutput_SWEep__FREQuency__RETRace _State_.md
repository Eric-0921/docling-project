# [:SOURce<hw>]:LFOutput:SWEep[:FREQuency]:RETRace <State>
Activates that the signal changes to the start frequency value while it is waiting for the next trigger event.

You can enable this feature, when you are working with sawtooth shapes in sweep mode "Single" or "External Single".

Parameters:

<State>

0 | 1 | OFF | ON

*RST:

0

Example:

TRIG0:SWE:SOUR SING

LFO:SWE:MODE SWE

LFO:SWE:SHAP SAWT

LFO:SWE:RETR ON

activates retrace function, that menas the frequency changes to the value at start frequency while waiting for the next trigger event.

Manual operation:

See "Retrace - LF Frequency Sweep" on page 230

