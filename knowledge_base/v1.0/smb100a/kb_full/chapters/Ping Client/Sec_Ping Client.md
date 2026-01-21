# Ping Client
The "Ping Client" page provides the ping utility to verify the connection between the LXI-compliant instrument and another device.

The ping is initiated from the instrument. Using the ICMP echo request and echo reply packets, the function checks whether the communication with a device via LAN works. Ping is useful for the diagnosis of IP network or router failures.

The ping utility is not password-protected.

To initiate a ping from the instrument to the device:

Enable "ICMP Ping" on the "Advanced LAN Configuration" page.

Operating Manual 1407.0806.32 ─ 23

44

R&S ® SMB100A

Getting Started

Preparing for Use

Select the "Ping Client" page.

In the "Destination Address" field, enter the IP address of the device you want to ping (without the ping command and without any further parameters), e.g. 10.113.1.203 .

Select "Submit".

![Picture](#/pictures/36)

