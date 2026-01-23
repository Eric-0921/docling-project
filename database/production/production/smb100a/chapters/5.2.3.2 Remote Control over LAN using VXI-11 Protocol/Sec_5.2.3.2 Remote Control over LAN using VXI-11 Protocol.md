# 5.2.3.2 Remote Control over LAN using VXI-11 Protocol
In this example, the I/O software library R&S VISA from Rohde & Schwarz is used to set up a LAN remote control link and remotely control the R&S SMB. R&S VISA is running on a controller PC with Windows operating system. When the connection is set up you can send commands to the instrument, and receive the responses.

The remote control connection requires a VISA installation but no additional hardware on the controller PC. The LAN I/O channel is selected at initialization time using the VISA resource string (also referred to as "address string"). A VISA alias (short name) is used to replace the complete resource string. The host address is either the R&S SMB's hostname or IP address. See also Chapter 5.1.3, "LAN Interface", on page 242.

Starting a Remote Control Session

Operating Manual 1407.0806.32 ─ 23

251

R&S ® SMB100A

Remote Control Basics

![Picture](#/pictures/304)

![Picture](#/pictures/305)

In this example, it is assumed that:

A LAN remote control link between the controller and the R&S SMB is already set up.

The R&S VISA program is installed on the remote PC, see "http://www.rohdeschwarz.com/rsvisa > RS VISA Release Notes".

