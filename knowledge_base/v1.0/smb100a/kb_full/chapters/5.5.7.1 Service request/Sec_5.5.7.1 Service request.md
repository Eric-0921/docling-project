# 5.5.7.1 Service request
Under certain circumstances, the instrument can send a service request (SRQ) to the controller. Usually this service request initiates an interrupt at the controller, to which the control program can react appropriately. An SRQ is always initiated if one or several of bits 2, 4 or 5 of the status byte are set and enabled in the SRE. Each of these bits combines the information of the error queue or the output buffer. To use the possibilities of the service request effectively, all bits should be set to "1" in the enable registers SRE and ESE.

Operating Manual 1407.0806.32 ─ 23

279

R&S ® SMB100A

Remote Control Basics

