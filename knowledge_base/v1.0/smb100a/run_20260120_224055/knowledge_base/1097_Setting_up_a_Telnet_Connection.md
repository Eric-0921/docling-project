---
chapter_index: 1097
title: "Setting_up_a_Telnet_Connection"
--- 

# Setting_up_a_Telnet_Connection

Setting up a Telnet Connection

To control the software, only a telnet program is required. The telnet program is part of every operating system.

To establish a Telnet connection with the R&S SMB, start the telnet program.

Enter the access string to connect to the instrument and confirm with [Enter]. The access string is composed of the open command short form) and the socket address. The socket address is a combination of the IP address or the host name of the R&S SMB and the number of the port configured for remote-control via telnet. The R&S SMB uses the port number 5025 for remote connection via Telnet.

Example: o 10.113.1.150 5025

Operating Manual 1407.0806.32 ─ 23

256

Remote Control Basics

R&S ® SMB100A

Starting a Remote Control Session

Telnet 10.113.1.150

口

X

Welcome to Microsoft Telnet Client

Escape Character is'CTRL++'

Micr0soft Telnet>o_10.113.1.150 5025

Connecting To 10.113.1.150..--

The connection to the instrument is set up and you can send remote-control commands.

Even if the cursor is not visible on the screen, enter blind a remote-control command and confirm with "Enter".

Telnet 10.113.1.150

口

X

三

Operating Manual 1407.0806.32 ─ 23

257

R&S ® SMB100A

Remote Control Basics

