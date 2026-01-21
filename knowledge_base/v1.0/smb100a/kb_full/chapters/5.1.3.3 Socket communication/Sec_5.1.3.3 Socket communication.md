# 5.1.3.3 Socket communication
An alternative way for remote control of the product is to establish a simple network communication using sockets. The socket communication, also referred to as "Raw Ethernet communication", does not necessarily require a VISA installation on the remote controller side. It is available by default on all operating systems.

The simplest way to establish socket communication is to use the built-in telnet program. The telnet program is part of every operating system and supports a communication with the software on a command-by-command basis. For more convenience and to enable automation by programs, user-defined sockets can be programmed.

![Picture](#/pictures/296)

Operating Manual 1407.0806.32 ─ 23

244

R&S ® SMB100A

Remote Control Basics

Remote Control Interfaces and Protocols

Socket connections are established on a specially defined port. The socket address is a combination of the IP address or the host name of the instrument and the number of the port configured for remote-control. Typically, the products of Rohde & Schwarz use port number 5025 for this purpose. The port is configured for communication on a command-to-command basis and for remote control from a program.

