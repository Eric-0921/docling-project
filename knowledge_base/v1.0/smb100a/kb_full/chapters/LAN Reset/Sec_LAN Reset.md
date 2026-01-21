# LAN Reset
Initiates the network configuration reset mechanism for the instrument and resets the hostname, MAC address, and IP address.

According to the LXI standard, a LAN Reset must place the following network settings to a default state:

| Parameter                      | Value                  |
|--------------------------------|------------------------|
| TCP/IP Mode                    | DHCP + Auto IP Address |
| Dynamic DNS                    | Enabled                |
| ICMP Ping                      | Enabled                |
| Password for LAN configuration | LxiWebIfc              |
