---
chapter_index: 1161
title: "Status_reporting_system"
--- 

# Status_reporting_system

Status reporting system

Figure 5-1: Graphical overview of the status registers hierarchy

Questionable

0

1

0

Output-Queue

Status

0

←

1

0

←

2

0

←

3

0

4

0

5

0

6

0

7

0

←

8

0

←

9

0

下1

10

0

11

Error-/Event-Queue

0

12

0

13

0

14

0

→

15

Standard

Operation Complete →

0

Event

fo

1

Status

Query Error →

2

Device Dependent Error →

3

ExecutionError→

4

+

Command Error →

5

Service Request Enable

User Request →

6

Power On →

7

Status Byte

Operation

Calibrating

0

Status

0

←

1

0

0

&

0

0

1

12345

0

下

2

Sweeping

3

2

T

QUES

0

4

MAV

→

0

→

5

ESB

0

→

6

RQS/MSS

x

0

→

7

0

→

8

OPER

&

7

0

→

9

0

←

10

0

←

11

0

12

Service Request

0

1

13

to controller at

0

下1

14

transition from 0 to 1

0

下1

15

OPER

= Operation Status Summary Bit

RQS/MSS = Service Request Generation

ESB

= Standard Event Status Summary Bit

MAV

= Message Available in Output Queue

QUES

= Questionable Status Summary Bit

2

= Error- /Event-Queue

1, 0

= not used

Note: This legend explains the abbreviations to the Status Byte Register.

The R&S SMB uses the following status registers:

Status Byte (STB) and Service Request Enable (SRE), see Chapter 5.5.3, "Status byte (STB) and service request enable register (SRE)", on page 277.

Operating Manual 1407.0806.32 ─ 23

274

R&S ® SMB100A

Remote Control Basics

Status reporting system

Standard Event Status , i.e. the Event status Register (ESR) and the Event Status Enable (ESE), see Chapter 5.5.4, "Event status register (ESR) and event status enable register (ESE)", on page 278.

Questionable Status and Operation Status , the (SCPI status registers, see Chapter 5.5.2, "Structure of a SCPI status register", on page 275, Chapter 5.5.5, "Questionable status register (STATus:QUEStionable)", on page 278 and Chapter 5.5.6, "Operation status register (STATus:OPERation)", on page 279.

