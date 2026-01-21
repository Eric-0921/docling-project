---
chapter_index: 90
title: "Installing_the_Ultr@VNC_application"
--- 

# Installing_the_Ultr@VNC_application

Installing the Ultr@VNC application

Download the program from the internet and copy it to a directory that can be accessed.

On the instrument, shut down firmware using the ALT+F4 key combination.

Double click on the setup file to start the installation. The setup wizard leads through the installation. This description focus only on the relevant settings.

Operating Manual 1407.0806.32 ─ 23

35

R&S ® SMB100A

Getting Started

Select installation of all components.

Setup-UItr@VNCRelease1.0.0RC18

SelectComponents

Wwhichcomponents should be installed?

Select the components you want to install;clear the componentsyou donot want to

install.ClickNextwhenyou areready tocontinue.

Full installation

UltraVNCServer

1.8MB

UltraVNCViewer

1.0MB

UltraVNC Repeater

0.1MB

Current selectionrequires at least 2.7MBofdisk space.

<Back

Next>

Cancel

In the "Additional Task Panel", enable all entries.

Setup-UItr@VNCRelease 1.0.0RC18

SelectAdditional Tasks

Which additional tasks should beperformed?

Select the additional tasksyou wouldlikeSetup toperformwhile installingUltr@vNC

Release 1.0.0 RC18,then clickNext

Serverconfiguration:

RegisterUtr@VNCServerasasystemservice

StartorrestartUltr@VNCservice

Additional icons:

CreateaUltr@vNCyiewer desktopicon

Createa Ultr@VNCServer desktop icon

CreateaUItr@VNCRepeater desktopicon

FileAssociations:

AssociatencfleswithUlt@VNCViewer

<Back

Next>

Cancel

A successful installation is indicated by a message.

WinVNC

TheWinvNCservice wassuccessfullyregistered

Theservice maybe startedfrom the Control Panel,and wil

automaticallyberunthenexttimethismachinelsreset

OK

At the same time a warning is displayed stating that a password must be set.

WinVNCError

WARNING:Thismachinehasnodefaultpasswordset.WinVNCwillpresent theDefault

Propertiesdialognowtoallowonetobeentered.

OK

Select "OK".

The "Default Local System Properties" panel opens.

Preparing for Use

Operating Manual 1407.0806.32 ─ 23

36

R&S ® SMB100A

Getting Started

Preparing for Use

WinVHC:DefaultLocal SystemProperties

Incoming Connections

Connection Settings

Accept Socket Connections

Force View Only(disable Viewers Inputs)

Password:

DisableLocal Inputs [Keyboard&Mouse)

RemoveDesktopWallpaper

DisplayNumber or Ports to use Auto

Display

N°

0

Update Handling

Ports

Main:

5900

Http:

5800

Poll Full Screen[Fast]

Poll Console

WindowsOnly

MSLogon

Poll ForegroundWindow-I

PollWindowUnderCursor

Received Only

EnableJava Viewer(Http Connection)

EnableXdmcp(X11 Connection]

SystemHookDll

Video Hook Driver

WhenLast ClientDisconnects

LowAccuracy[Turbo Speed]

Do Nothing

DSM Plugin

LockWorkstation(W2K]

Use

No Plugin detected

Config

Logoff Workstation

Misc.

Share onlytheWindowNamed:

Share

Enable Blank Monitor onViewer Request

Enable File Transfer

Queryonincoming connection

Log debug infos to the WinvNc.log file

DisplayQueryWindow

Timeout:/10

S

Allow Loopback Connections

Default ServerScreen

11

OK

Apply

Cancel

Enter a password with a length of at least five digits.

This password is used on the remote computer to access the instrument. Other settings may be changed according to the user-specific security requirements.

After the installation the Ultr@VNC program is automatically started together with the operating system. On mouse over, the IP address of the instrument is indicated.

This IP address and the user-defined password are the prerequisites to enable remote access on the remote computer. Terminated connection is indicated by changed icon color.

