---
chapter_index: 379
title: "Provided_security_services_are:"
--- 

# Provided_security_services_are:

Provided security services are:

Password management secures controlled user access to the instrument

Operating Manual 1407.0806.32 ─ 23

114

R&S ® SMB100A

Instrument Function

General Instrument Settings

With the two-step password concept, you can assign a user-defined password for the operating system, as well as a security password for accessing the mass storage of the instrument.

For more information concerning the security password, see the description Resolving Security Issues when Working with an R&S SMB . You can find this document on the R&S SMB product page at "Downloads" > "Manuals".

LAN Services secures controlled network access. You can individually lock and unlock the supported LAN interface services, see "LAN Services" on page 117. Remote control via LAN interface requires that the interface is activated, but you

can enable the required services specifically.

General security parameters as:

-USB Storage secures controlled access to the mass memory of the instrument.

-Volatile mode protects against modification or deletion of data in the file system.

-Annotation frequency and amplitude prevents reading the display.

-User Interface prevents front panel operation and/or reading the display

-Secure Update Policy check that verifies the integrity and origin of the firmware package to be installed.

-Bluetooth enables operation of the instrument via Bluetooth.

Changing the password for the operating system or the security password requires that you enter the old password, the new password and that you confirm the new password.

To assign the password, press the "Accept" button. This action can not be undone! Keep also in mind, that security settings are never reset, even if you perform a factory preset.

To access this dialog, press the [SETUP] or [MENU] key and select "Protection " > "Security".

Operating Manual 1407.0806.32 ─ 23

115

R&S ® SMB100A

Instrument Function

Security

Change User Password

Valid for VNC, FTP and SMB (Samba) access

User Name

instrument

OldPassword

NewPassword

ConfirmPassword

Change Password

Change Security Password

Old Password

New Password

ConfirmPassword

ChangePassword

SecuritySettings

LAN Services

USBStorage

Enabled

VolatileMode

Enabled

Annotation Frequency

Enabled

Annotation Amplitude

Enabled

User Interface

Enabled

SecureUpdatePolicy

Confirm

Security Password

Accept

Bluetooth

BluetoothPin

The "Security" dialog comprises the parameters for configuring the passwords, as well as the security settings of the mass storage and the LAN services.

The settings in this dialog will not be assigned until you enter the Security Password and confirm with the Accept button.

