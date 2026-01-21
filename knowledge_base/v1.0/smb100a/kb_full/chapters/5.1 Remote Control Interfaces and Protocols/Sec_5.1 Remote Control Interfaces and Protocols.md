# 5.1 Remote Control Interfaces and Protocols
The instrument supports different interfaces for remote control. The following table gives an overview.

| Interface                     | Protocols, VISA *) address string                                                                                                                                                                                                                                                                                                                       | Remarks                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Local Area Net- work (LAN)    | Protocols: ● HiSLIP High-Speed LAN Instrument Protocol (IVI-6.1) VISA *) address string: TCPIP::host address:: hislip0[::INSTR] ● VXI-11 VISA *) address string: TCPIP::host address[:: LAN device name][::INSTR] ● socket communication (Raw Ethernet, simple telnet) VISA *) address string: TCPIP::host address[:: LAN device name]::<port>:: SOCKET | A LAN connector is located on the front or rear panel of the instrument, or both. The interface is based on TCP/IP and supports various proto- cols. For a description of the protocols refer to: ● Chapter 5.1.3.1, "HiSLIP protocol", on page 244 ● Chapter 5.1.3.2, "VXI-11 protocol", on page 244 ● Chapter 5.1.3.3, "Socket communication", on page 244 |
| Serial Interface              | VISA *) address string: ASRL[0-9][::INSTR]                                                                                                                                                                                                                                                                                                              | For a description of the interface, refer to Chapter 5.1.5, "Serial Interface", on page 246.                                                                                                                                                                                                                                                                 |
| GPIB (IEC/IEEE Bus Interface) | VISA *) address string: GPIB::primary address[::INSTR] (no secondary address)                                                                                                                                                                                                                                                                           | Optional GPIB bus interfaces according to standard IEC 625.1/ IEEE 488.1 are located on the rear panel of the instrument. For a description of the interface, refer to Chapter 5.1.6, "GPIB Interface (IEC/IEEE Bus Interface)", on page 246. Note: Within this interface description, the term GPIB is used as a synonym for the IEC/IEEE bus interface.    |
![Picture](#/pictures/294)

Rohde & Schwarz provides the standardized I/O software library R&S VISA for communication via TCP/IP (LAN: HiSlip, VXI-11 and raw socket) or USB (USBTMC) interfaces.

R&S VISA is available for download at the Rohde & Schwarz website http:// www.rohde-schwarz.com/rsvisa.

How to configure the remote control interfaces, see Chapter 5.2, "Starting a Remote Control Session", on page 249.

Operating Manual 1407.0806.32 ─ 23

240

R&S ® SMB100A

Remote Control Basics

Remote Control Interfaces and Protocols

