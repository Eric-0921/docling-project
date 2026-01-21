# 3.1.16 Remote Access via an External Controller
The R&S SMB can be remote accessed from a remote computer (external controller) via a network link. This allows convenient operation of the instrument from the desktop although the instrument is integrated in a rack somewhere else.

![Picture](#/pictures/15)

For an overview of the instrument's operating concept and the different ways to control and operate the instrument, see Chapter 3.4, "System Overview", on page 62.

There are different ways to establish a remote access connection to the signal generator but all of them require an established LAN connection between the instrument and the remote computer. The simplest way to remote access the instrument is to use a Web browser, such as Windows Internet Explorer or Mozilla Firefox for instance. Alternatively a remote access via a special application can be used.

For example, the free-of-charge program Ultr@VNC for PCs with Linux/Unix or Windows operating system is available for setting up the remote access connection. Using this application requires additional installation.

Operating Manual 1407.0806.32 ─ 23

32

R&S ® SMB100A

Getting Started

Preparing for Use

![Picture](#/pictures/16)

See the following table for an overview of the different ways to establish a remote access connection to the signal generator.

| Remote access via                                                                                                                                                                                  | LAN connec- tion   | Installation of the additional application   | Installation of the additional application                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|-----------------------------------------------------------------------|
|                                                                                                                                                                                                    | LAN connec- tion   | on the instrument                            | on the remote computer                                                |
| Any web browser for example Windows Internet Explorer or Mozilla Firefox, see Chapter 3.1.16.1, "Using a Web Browser for Remote Access", on page 33                                                | required           | no                                           | Java Runtime must be installed and activated in the browser settings. |
| Web browser with HTML5 for example LXI Browser, see "Web Control" on page 45                                                                                                                       | required           | no                                           | Web sockets must be supported.                                        |
| VNC Client for example Ultr@VNC or other dedicated client software for PCs with Linux/Unix or Windows operating system see Chapter 3.1.16.2, "Remote Access via a VNC Client Software", on page 34 | required           | required                                     | VNC Viewer required                                                   |
When the connection is set up with a VNC client software (Ultr@VNC), direct control on the instrument is possible while remote access is established.

For return to direct operation on the instrument, the connection must be cut. After cutting the connection, it is still enabled and can be established again any time. The connection is disabled only after deactivation of the program.

This section gives an information on how to use the Web browser for remote access, how to install the applications for remote access and how to establish the connection between the instrument and an external computer with Windows operating system. Remote access via an external computer with Linux/Unix operating system is performed accordingly.

