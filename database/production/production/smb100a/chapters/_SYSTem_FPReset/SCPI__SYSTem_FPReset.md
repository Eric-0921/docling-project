# :SYSTem:FPReset
Triggers an instrument reset to the original state of delivery.

Note: "Factory Preset" resets the "Remote Channel" and network settings to the default values.

Executing "Factory Preset" via remote control terminates the connection to the instrument, if these settings had been configured to values different to the default ones.

The factory preset function resets nearly all instrument settings. In addition to the regular preset by means of the [PRESET] key, a "Factory Preset" resets also the following values:

Reference frequency settings ("Ref Oscillator" menu)

Power on settings ("Level/EMF" menu)

Network settings including hostname ("Setup" menu)

Remote channel settings including GPIB address ("Setup" menu)

Start/Stop display update ("Setup" menu)

Display and keyboard settings ("Setup" menu).

Operating Manual 1407.0806.32 ─ 23

289

R&S ® SMB100A

Remote Control Commands

CALibration Subsystem

To maintain security, password settings and all settings protected by these passwords like disabled USB and LAN connections are not changed.

Not affected by the "Factory Preset" are also user data, lists or instrument settings files, created for example by means of the Save/Recall function.

Example:

SYST:FPR

All instrument settings (also the settings that are not currently active) are reset to the factory values.

Usage:

Event

Manual operation:

See "Factory Preset" on page 122

