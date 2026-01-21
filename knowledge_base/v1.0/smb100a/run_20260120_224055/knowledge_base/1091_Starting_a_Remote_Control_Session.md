---
chapter_index: 1091
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

Operating Manual 1407.0806.32 ─ 23

253

R&S ® SMB100A

Remote Control Basics

In the menu bar, select "RsVisaConfig".

RsVisaConfigure - 5.5.4

口

X

Resource identifier

Alias

In the toolbar, select "+" to access the "VISA Resource String Composer".

Fill in the "Alias" name, the "VISA Resource String" and the "Device IP Address or host name" as shown in the figure, and confirm with "OK".

+ISA Resource String Composer

Resource String

Build Interface

Alias

Interface Type

Rohde&Schwarz_SignalGenerator

VXI-11

VISA Resource String

Board Number

TCPIP0::10.113.151.1::instr0::INSTR

0

TCP/IP

Device IP Address or hostname

10.113.151.1

Device Id

0

OK

Cancel

The "Alias" name is assigned to the instrument.

RsVisaConfigure - 5.5.4

口

X

Resourceidentifier

Alias

TCPIP0::10.113.151

Rohde&Schwarz_SignalGenerator

Close the dialog.

The R&S SMB is now registered in the program and can be addressed via the resource string or alias name.

In the main window, select "Connect".

R&S VISA establishes the connection to the R&S SMB.

Now you can send settings to configure the instrument and receive its responses.

