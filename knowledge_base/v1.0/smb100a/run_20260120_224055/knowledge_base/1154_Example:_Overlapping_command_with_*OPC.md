---
chapter_index: 1154
title: "Example:_Overlapping_command_with_*OPC"
--- 

# Example:_Overlapping_command_with_*OPC

Example: Overlapping command with *OPC

The instrument implements INITiate[:IMMediate] as an overlapped command. Assuming that INITiate[:IMMediate] takes longer to execute than *OPC , sending the following command sequence results in initiating a sweep and, after some time, setting the OPC bit in the ESR :

INIT; *OPC.

Sending the following commands still initiates a sweep:

INIT; *OPC; *CLS

However, since the operation is still pending when the instrument executes *CLS , forcing it into the "Operation Complete Command Idle" state (OCIS), *OPC is effectively skipped. The OPC bit is not set until the instrument executes another *OPC command.

