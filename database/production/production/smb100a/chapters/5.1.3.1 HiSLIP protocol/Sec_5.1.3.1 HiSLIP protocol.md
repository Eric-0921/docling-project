# 5.1.3.1 HiSLIP protocol
The High Speed LAN Instrument Protocol (HiSLIP) is the successor protocol for VXI-11 for TCP-based instruments specified by the IVI foundation. The protocol uses two TCP sockets for a single connection - one for fast data transfer, the other for non-sequential control commands (e.g. Device Clear or SRQ ).

HiSLIP has the following characteristics:

High performance as with raw socket network connections

Compatible IEEE 488.2 support for Message Exchange Protocol, Device Clear, Serial Poll, Remote/Local, Trigger, and Service Request

Uses a single IANA registered port (4880), which simplifies the configuration of firewalls

Supports simultaneous access of multiple users by providing versatile locking mechanisms

Usable for IPv6 or IPv4 networks

Using VXI-11, each operation is blocked until a VXI-11 instrument handshake returns. However, using HiSLIP, data is sent to the instrument using the "fire and forget" method with immediate return. Thus, a successful return of a VISA operation such as viWrite() guarantees only that the command is delivered to the instrument's TCP/IP buffers. There is no confirmation, that the instrument has started or finished the requested command.

For more information see also the application note:

1MA208: Fast Remote Instrument Control with HiSLIP

