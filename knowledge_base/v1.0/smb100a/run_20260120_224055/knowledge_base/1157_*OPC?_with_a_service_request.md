---
chapter_index: 1157
title: "*OPC?_with_a_service_request"
--- 

# *OPC?_with_a_service_request

*OPC? with a service request

Execute *SRE 16

Sets the Message Available bit (MAV - bit No. 4) of the Service Request Enable Register (SRE) to 1 to enable MAV service request.

Send the overlapped command with *OPC?

Example: INIT ;  *OPC?

Wait for an MAV service request.

The service request indicates that the overlapped command has finished.

