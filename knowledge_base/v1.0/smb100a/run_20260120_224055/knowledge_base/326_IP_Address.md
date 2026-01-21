---
chapter_index: 326
title: "IP_Address"
--- 

# IP_Address

IP Address

Displays the IP address.

By default, the R&S SMB is configured to use dynamic TCP/IP configuration and to obtain the whole address information automatically.

If the network does not support DHCP or the attempt does not succeed, the instrument tries to obtain the IP address via Zeroconf (APIPA) protocol. IP addresses assigned via Zeroconf start with the number blocks 169.254.*.* .

Note: An IP address that is assigned via the Zeroconf protocol while the network requires an IP address assigned via the DHCP server may cause network connection failures.

See Chapter 9.5, "Resolving network connection failures", on page 505.

To assign the IP address manually, select Address Mode "Static".

Remote command:

:SYSTem:COMMunicate:NETWork:IPADdress on page 446

