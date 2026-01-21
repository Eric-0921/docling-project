# To access the file system of the R&S SMB via ftp
If the R&S SMB is connected to a LAN and the required configurations are completed, you can use File Transfer Protocol (ftp) to access the file system and to transfer files from and to the instrument.

Connect the instrument and the remote PC to a LAN.

Find out the "IP Address" of the instrument:

Select "Setup > Environment > Network Settings".

Write down the "IP Address" of the instrument, e.g. 10.113.10.105 .

On the remote PC, start the Windows Explorer.

In the address field, enter ftp://<"IP Address" of the Instrument> , e.g. ftp://10.113.10.105

A log on dialog opens and requests a password.

Tip: Default password. The FTP file access use the user instrument with default password instrument .

It is highly recommended that you change the user password in the "Security" dialog before connecting the instrument to the network!

See Chapter 4.2.3.14, "Security", on page 114.

Enter the password to access the /var/user/share directory.

Operating Manual 1407.0806.32 ─ 23

134

R&S ® SMB100A

Instrument Function

![Picture](#/pictures/165)

You can access the files in the /var/user/ directory, perform standard function like creating directory, etc.

Open the /var/user/share directory and create a new directory, e.g. testftp .

On the instrument, press the [File] key and open the /var/user/share directory. The dialog displays the testftp dircetory.

![Picture](#/pictures/166)

