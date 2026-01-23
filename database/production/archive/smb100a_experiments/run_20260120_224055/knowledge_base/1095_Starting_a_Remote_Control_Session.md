---
chapter_index: 1095
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

The instrument response is 4000000000 , i.e. the frequency is returned in Hz.

While remote control is active, the "Remote" icon in the status bar indicates that the instrument is in remote control mode. The operation via the front panel or via mouse and keyboard are locked, allowing a remote control program to be performed without interruption.

On the display, keys and entry fields are grayed out and cannot be activated or modified, but you can still open dialogs, for example to verify settings.

To disable the access to the dialogs, use the command SYST:KLOC ON .

To prevent unintentional return to manual operation, use the command &LLO . See also Chapter 5.1.3.4, "LAN interface messages", on page 245.

The instrument switches to "Remote LLO" state. The [LOCAL] key is disabled.

To enable the [LOCAL] key, use the command &GTR .

To return to manual operation, see Chapter 5.2.2, "Returning to Manual Operation", on page 250.

Tip: Switching from manual operation to remote control and vice versa does not affect the other instrument settings.

