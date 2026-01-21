---
chapter_index: 1089
title: "Configuring_the_controller"
--- 

# Configuring_the_controller

Configuring the controller

To remote control the R&S SMB, we use the R&S VISA Tester application.

The instrument is preconfigured for networks using DHCP (dynamic host configuration protocol). If this configuration is used, enter the computer name in the position of the IP address.

To enable the external controller to communicate with the R&S SMB via TCP/IP protocol, set up a remote control link as follows:

Make sure that the controller and the instrument are connected in the network (network cable) and switched on.

On the controller, start "R&S VISA > Tester 32bit" or "R&S VISA > Tester 64bit", respectively.

RsVisaTester 5.5.4 Visa from Rohde & Schwarz GmbH (5.5.4)

口

口

Find Resource Change Log File RsVisa Config Choose Visa Implementation

Resource

Timneout

Current log ile

show Log

Connect

2000

日

Open Log

visaTesterllog20151109_104402.txt

口

]Write Log

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

8

1 μs VI_SUCCESS viGetAttribute(sessionid= ..

9

1 μs V_SUCCESS viGetAttribute(sessionid=..

10

7μs VI_SUCCESS viSetAttribute(sessionid=1..

Write

Read

Query

Clear History

11

4 μs V_SUCCESS viGetAttribute(sessionid= ..

send End

12

8μsVI_SUCCESS viGetAttribute(sessionid=

13

11 μs VI_SUCCESS viGetAttribute(sessionid=..

14

14 ms VI_SUCCESS viOpen(sesn= 3, rsrc= TCPI..

15

13 μs VI_SUCCESS viSetAttribute(sessionid= 4

16

1 ms VI_SUCCESS viClose(sessionid= 4)

17

13 ms VI_SUCCESS viOpen(sesn= 3, rsrc= TCPI

18

7 μs VI_SUCCESS viSetAttribute(sessionid= 5

19

1 ms VI_SUCCESS viClose(sessionid= 5)

20

7 μs V_SUCCESS viGetAttribute(sessionid= ..

21

1 μs VI_SUCCESS viGetAttribute(sessionid= ..

22

1 μsVI_SUCCESS viGetAttribute(sessionid=

Clear Text

Read count1024

日

23

9 μs VI_SUCCESS viSetAttribute(sessionid= 3

Live Mode

Lines: 23

Clear

Read STB

Clear

View Mode

Displayed: 16

OX-..

Status: I_SUCCESS

In the menu bar, select "Choose VISA Implementation > Rohde & Schwarz Visa".

