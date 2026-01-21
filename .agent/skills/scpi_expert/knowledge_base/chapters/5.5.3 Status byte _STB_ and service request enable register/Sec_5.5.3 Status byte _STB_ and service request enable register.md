# 5.5.3 Status byte (STB) and service request enable register (SRE)
The STatus Byte (STB) is already defined in IEEE 488.2. It provides a rough overview of the instrument status by collecting the pieces of information of the lower registers. A special feature is that bit 6 acts as the sum bit of the remaining bits of the status byte.

The STB is read using the command *STB? or a serial poll.

The STatus Byte (STB) is linked to the Service Request Enable (SRE) register. Each bit of the STB is assigned a bit in the SRE. Bit 6 of the SRE is ignored. If a bit is set in the SRE and the associated bit in the STB changes from 0 to 1, a service request (SRQ) is generated. The SRE can be set using the command *SRE and read using the command *SRE? .

| Bit No.   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0...1     | Not used                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2         | Error Queue not empty The bit is set when an entry is made in the error queue. If this bit is enabled by the SRE, each entry of the error queue generates a service request. Thus an error can be recognized and specified in greater detail by polling the error queue. The poll provides an informative error mes- sage. This procedure is to be recommended since it considerably reduces the problems involved with remote control. |
| 3         | QUEStionable status register summary bit The bit is set if an EVENt bit is set in the QUEStionable status register and the associated ENABle bit is set to 1. A set bit indicates a questionable instrument status, which can be speci- fied in greater detail by querying the STATus:QUEStionable status register.                                                                                                                     |
| 4         | MAV bit (message available) The bit is set if a message is available in the output queue which can be read. This bit can be used to enable data to be automatically read from the instrument to the controller.                                                                                                                                                                                                                         |
| 5         | ESB bit Sum bit of the event status register. It is set if one of the bits in the event status register is set and enabled in the event status enable register. Setting of this bit indicates a serious error which can be specified in greater detail by polling the event status register.                                                                                                                                            |
| 6         | MSS bit (main status summary bit) The bit is set if the instrument triggers a service request. This is the case if one of the other bits of this registers is set together with its mask bit in the service request enable register SRE.                                                                                                                                                                                                |
| 7         | STATus:OPERation status register summary bit The bit is set if an EVENt bit is set in the OPERation status register and the associated ENABle bit is set to 1. A set bit indicates that the instrument is just performing an action. The type of action can be determined by querying the STATus:OPERation status register.                                                                                                             |
Operating Manual 1407.0806.32 ─ 23

277

R&S ® SMB100A

Remote Control Basics

Status reporting system

