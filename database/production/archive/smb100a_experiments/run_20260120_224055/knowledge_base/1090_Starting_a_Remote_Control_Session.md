---
chapter_index: 1090
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

Operating Manual 1407.0806.32 ─ 23

252

R&S ® SMB100A

Remote Control Basics

Choose VISA implem

X

Rohde&SchwarzVisa

Default Visa

OK

Cancel

Select "Rohde & Schwarz Visa" and confirm with "OK".

In the menu bar, select "Find Resource" to search for the instrument in the LAN.

Find and select resource

X

Resource

Find Resources

LXI (mDNS)

VXI-11

1000

Select

*

Cancel

Select "VXI-11" and "Find Resources".

R&S VISA scans the network for connected instruments and lists all detected instuments in the "Resource" list.

Note: The search may take some time, particularly in large networks.

Select the required instrument and confirm with "Select".

Find and selectresource

Resource

Find Resources

TCPIP0::10.113.1.151

LXI (mDNS)

TCPIP0:10.113.1.151:inst0:INSTR

VXI-11

>

TCPIP0::10.113.1.154

>

TCPIP0::10.113.1.179

1000

>

TCPIP0:10.113.1.188

>

TCPIP0::10.113.1.18

TCPIP0::10.113.1.23

Select

TCPIP0::10.113.1.151::inst0::INSTR

*

Cancel

The "Find and select resource" dialog closes and R&S VISA indicates the instruments IP address in the "Resource" field of the main application window.

As an alternative to the IP address, you can assign an alias name to the R&S SMB:

