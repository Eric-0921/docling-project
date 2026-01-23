---
chapter_index: 1094
title: "Starting_a_remote_control_over_LAN_(using_VXI-11)"
--- 

# Starting_a_remote_control_over_LAN_(using_VXI-11)

Starting a remote control over LAN (using VXI-11)

To set the instrument to remote control, you can use the addressed command &GTR , or send any command from the controller.

Start the R&S VISA Tester and establish the connection to the R&S SMB, see "Configuring the controller" on page 252.

In the R&S VISA "Basics" tab, enter a SCPI command, e.g. "*IDN?" and confirm with "Query".

The instrument is switched to remote control when it receives a command from the controller.

Select "Read" to obtain the instrument response.

RsVisaTester 5.5.4 Visa from Rohde & Schwarz GmbH (5.5.4)

口

Find Resource Change Log File RsVisa Config Choose Visa Implementation

Resource

Timneout

Current log File

show Log

TCPIP0:10.113.1.150: :instO:INSTR

Disconnect

2000

日

Open Log

visaTester\log20151112_124312.txt

Write Log

Basics

Locking

Attributes

Events

Gpib

Tests

Line

Duration

Status

Visa Operation

10

452 μs VI_SUCCESS viWrite(sessionid= 4,buf= .

*IDN?

Write

Read

Query

Clear History

Send End

Clear Text

Read count 1024

日

Live Mode

Lines: 10

Read STB

Clear

Clear

View Mode

Displayed: 1

OX-..

Status: I_SUCCESS

Tip: If the "Show Log" checkbox is checked R&S VISA displays each VISA function call in the log-view on the left. If you check the "Write Log" checkbox the log-view entry is written to the log file as well. You can operate the log-view in two modes: the "Live Mode" shows only the most recent messages whereas the "View Mode" allows you to scroll the history.

To set, e.g. the frequency, enter SOUR1:FREQ 4 GHz and select "Write". To check the performed setting, SOUR1:FREQ? and select "Read".

Operating Manual 1407.0806.32 ─ 23

255

R&S ® SMB100A

Remote Control Basics

