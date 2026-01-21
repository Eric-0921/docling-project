# :DISPlay:PSAVe[:STATe] <State>
Activates the screen-save mode of the display.

DISPlay Subsystem

Operating Manual 1407.0806.32 ─ 23

296

R&S ® SMB100A

Remote Control Commands

FORMat Subsystem

If activated, the display including backlight is switched off after the wait time elapses and if no entries via front panel, external mouse or external keyboard are made. To set the wait time, use command :DISPlay:PSAVe:HOLDoff .

This mode is recommended for protecting the display, especially if you operate the instrument via remote control.


## Parameters:
<State>

0 | 1 | OFF | ON

*RST:

n.a. (factory preset: 0)

Example:

DISP:PSAV ON

Activates screen saver mode.

Manual operation:

See "Screen Saver Active" on page 108

