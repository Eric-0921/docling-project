---
chapter_index: 1059
title: "Example:"
--- 

# Example:

Example:

Instrument has the IP address 192.1.2.3 ; the valid resource string using VXI-11 protocol is:

TCPIP::192.1.2.3::INSTR

The DNS host name is RSSM1 ; the valid resource string is:

TCPIP::RSSM1::hislip0 (HISLIP)
      TCPIP::RSSM1::INSTR (VXI-11)

A raw socket connection can be established using: TCPIP::192.1.2.3::5025::SOCKET

