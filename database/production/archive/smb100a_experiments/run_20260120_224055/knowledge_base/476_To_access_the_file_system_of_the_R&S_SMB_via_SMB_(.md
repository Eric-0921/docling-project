---
chapter_index: 476
title: "To_access_the_file_system_of_the_R&S_SMB_via_SMB_("
--- 

# To_access_the_file_system_of_the_R&S_SMB_via_SMB_(

To access the file system of the R&S SMB via SMB (Samba)

The SMB (Samba) protocol is an alternative way to access the file system of the instrument form a remote PC, if both the instrument and the PC are connected to a LAN.

Connect the instrument and the remote PC to a LAN.

Find out the "IP Address" of the instrument:

Select "Setup > Environment > Network Settings".

Write down the "IP Address" of the instrument, e.g. 10.113.10.105 .

On the remote PC, start the Windows Explorer and open the "Map Network Drive" dialog.

Select a valid "Drive", e.g. W .

In the "Folder" field, enter:

//<"IP Address" of the Instrument>/share or //<"Hostname" of the Instrument>/share , e.g. //10.113.10.105/share c) Select "Finish".

A log on dialog opens and requests an user name and a password.

General Instrument Settings

Operating Manual 1407.0806.32 ─ 23

135

R&S ® SMB100A

Instrument Function

RF Block

Enter the user name and the password of your instrument.

The default user name and password is instrument .

Tip: Default password. The SAMBA/SMB file access use the user instrument with default password instrument .

It is highly recommended that you change the user password in the "Security" dialog before connecting the instrument to the network!

See Chapter 4.2.3.14, "Security", on page 114.

The /var/user/share directory of the instrument is mapped to and displayed as a network drive of the remote PC.

You can access the files in this directory, perform standard function like creating directory, storing files, etc.

