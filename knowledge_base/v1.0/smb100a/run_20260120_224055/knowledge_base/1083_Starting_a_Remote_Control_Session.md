---
chapter_index: 1083
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

The instrument remains in the remote state until it is reset to the local state, see Chapter 5.2.2, "Returning to Manual Operation", on page 250).

Tip: Switching from manual operation to remote control and vice versa does not affect the other instrument settings.

Although operation via front panel, mouse and keyboard is disabled, the dialog boxes can still be opened, for example to verify settings. The buttons and setting fields are grayed out and cannot be activated.

Additionally, you can disable the access to the dialogs with the command SYST:KLOC ON to protect the instrument against unauthorized readings.

To prevent unintentional return to manual operation, disable the [LOCAL] key of the instrument with the &LLO command (see Chapter 5.1.3.4, "LAN interface messages", on page 245).

The instrument switches to "REM-LLO" state.

The automatic transition from local state to remote state by a subsequent remote command, and the command *GTL are disabled.

To return to manual mode is only possible via remote control.

Unlock the [LOCAL] key with &GTR .

