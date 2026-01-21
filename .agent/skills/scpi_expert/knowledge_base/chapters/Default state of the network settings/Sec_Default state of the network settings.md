# Default state of the network settings
According to the LXI standard, an LCI must set the following parameters to a default state.

| Parameter                      | Value                  |
|--------------------------------|------------------------|
| TCP/IP Mode                    | DHCP + Auto IP Address |
| Dynamic DNS                    | Enabled                |
| ICMP Ping                      | Enabled                |
| Password for LAN configuration | LxiWebIfc              |
The LCI for the R&S SMB also resets the following parameters:

| Parameter        | Value                           |
|------------------|---------------------------------|
| Hostname         | <Instrument-specific host name> |
| Description      | Vector Signal Generator         |
| Negotiation      | Auto Detect                     |
| VXI-11 Discovery | Enabled                         |
The LAN settings are configured using the instrument's "LXI Browser Interface".

