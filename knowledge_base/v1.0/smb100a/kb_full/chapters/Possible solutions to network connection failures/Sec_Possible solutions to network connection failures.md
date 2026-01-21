# Possible solutions to network connection failures
NOTICE! Connecting to the network can cause network failure. Errors can affect the entire network.

Operating Manual 1407.0806.32 ─ 23

505

R&S ® SMB100A

Status Information, Error Messages and Troubleshooting

Obtaining Technical Support

Consult your network administrator before performing the following tasks:

Connecting the instrument to the network

Configuring the network

Changing IP addresses

Try out the following to resolve network connection failures:

Check the network infrastructure. Exchange connecting cables, if obvious damage is visible.

Observe the link status LED on the R&S SMB or the connected network device. The link status LED is located next to the LAN connector. If a link failure is detected, connect the instrument to a different device port or to a different network device.

Check whether the LAN interface and the required LAN services are enabled. See "LAN Services" on page 117.

If the IP address is set manually (no DHCP) or obtained via the Zeroconf (APIPA) protocol:

-Check whether the IP address of the instrument is within the network's address range.

-Check whether the IP address is valid.

See "IP Address" on page 106.

