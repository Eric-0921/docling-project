# Automatic Level Control is deactivated with pulse modulation!
When pulse modulation is activated, the R&S SMB deactivates ALC automatically ("ALC OFF", i.e. switches to "Sample & Hold" state).

The "Sample & Hold" state opens the ALC loop, and disables the automatic control of the output level. The level modulator is set directly.

However, to correct the output level, the R&S SMB executes a "Sample & Hold" measurement after each change of frequency or level settings.

The level is decreased by 30 dB during "Sample & Hold" measurement.

