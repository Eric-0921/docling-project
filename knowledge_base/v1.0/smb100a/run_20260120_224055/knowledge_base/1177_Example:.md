---
chapter_index: 1177
title: "Example:"
--- 

# Example:

Example:

Use command *OPC to generate an SRQ .

*ESE 1 - set bit 0 of ESE (Operation Complete)

*SRE 32 - set bit 5 of SRE (ESB).

After its settings have been completed, the instrument generates an SRQ.

The SRQ is the only possibility for the instrument to become active on its own. Each controller program should set the instrument such that a service request is initiated in the case of malfunction. The program should react appropriately to the service request.

