---
chapter_index: 1158
title: "Event_status_enable_register_(ESE)"
--- 

# Event_status_enable_register_(ESE)

Event status enable register (ESE)

Execute *ESE 1 Sets the OPC mask bit (bit No. 0) of the Standard Event Status Register (ESR) to 1

Send the overlapped command without *OPC , *OPC? or *WAI . Example: INIT; *OPC?

Poll the operation complete state periodically (with a timer) using the sequence: *OPC; *ESR?

A return value (LSB) of 1 indicates that the overlapped command has finished.

