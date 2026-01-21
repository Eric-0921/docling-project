# *OPC with a service request
Execute *ESE 1 Sets the OPC mask bit (bit No. 0) of the Standard Event Status Register (ESR) to 1

Execute *SRE 32

Operating Manual 1407.0806.32 ─ 23

272

R&S ® SMB100A

Remote Control Basics

Status reporting system

Sets the Event Status Bit (ESB - bit No. 5) of the Service Request Enable Register (SRE) to 1 to enable ESB service request.

Send the overlapped command with *OPC

Wait for an ESB service request.

Example: INIT;  *OPC

The service request indicates that the overlapped command has finished.

