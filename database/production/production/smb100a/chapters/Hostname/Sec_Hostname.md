# Hostname
Displays the host name.

Each instrument is delivered with an assigned host name, a logical name which can be used instead of the IP address. With the default network settings, the IP address is allocated by the DHCP server. This address may change each time the instrument is reconnected. Unlike the IP address, the host name does not change.

Operating Manual 1407.0806.32 ─ 23

105

R&S ® SMB100A

Instrument Function

General Instrument Settings

Note: Since the host name of the instrument is a protected parameter, you must first unlock protection level 1 to enable the entry (see Chapter 4.2.3.13, "Protection", on page 113).

It is recommended that you neither change the default network settings nor the host name in order to avoid problems with the network connection.

However, if you change the host name be sure to use an unique name.

Remote command:

:SYSTem:COMMunicate:NETWork[:COMMon]:HOSTname on page 445

