# 4.3.7.2 RF Frequency Sweep
The dialog enables you to activate and configure a sweep for the RF frequency.

To open the "RF Frequency Sweep" dialog, select "RF > Configure > RF Frequency Sweep" or use the [MENU] key under "RF".

In the top section of the dialog, the RF sweep is activated and the sweep mode is selected.

The buttons are used to reset the RF sweep (all sweep modes) or to execute the RF sweep ("Single" mode).

The sweep range, sweep spacing and dwell time are set in the bottom section.

For the frequency sweep, an output signal at the [LF] connector can be activated. It provides a linear voltage ramp from start to stop of the sweep. The output voltage can be used for example to control an oscilloscope.

You can configure the sweep range of the RF sweep in two ways, either by entering the "Start" and "Stop" values or by entering the "Center" frequency and the "Span".

The two sets of parameters correlate as follows:

"Start Freq" = "Center Freq" - "Span"/2

"Stop Freq" = "Center Freq" + "Span"/2

"Center Freq" = ("Start Freq" + [Stop Freq])/2

"Span" = "Stop Freq" - "Start Freq"

Operating Manual 1407.0806.32 ─ 23

179

R&S ® SMB100A

Instrument Function

![Picture](#/pictures/231)

