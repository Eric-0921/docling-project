# Advanced LAN Configuration
The "Advanced Config" page provides LAN settings that are not declared mandatory by the LXI standard.

Operating Manual 1407.0806.32 ─ 23

43

R&S ® SMB100A

Getting Started

Preparing for Use

![Picture](#/pictures/35)

The following advanced parameters are available:

"mDNS and DNS-SD": The additional protocols "multicast DNS" and "DNS service discovery" are used for device communication in zero configuration networks, working without DNS and DHCP.

"ICMP Ping enabled": Must be enabled to use the ping utility. If you disable this setting, the instrument does not answer ping requests. The setting does not affect the LXI ping client. You can ping other hosts from the instrument, even if the setting is disabled.

"VXI-11 Discovery": Must be enabled to detect the instrument in the LAN. If you disable this setting, the instrument cannot be detected by the VXI-11 discovery protocol mechanism. The setting does not affect other detection mechanisms. Setting up a VXI-11 connection via the IP address or the host name is independent of this setting.

