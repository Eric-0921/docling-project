# STEReo:DIRect "BIN=<x>"
Defines and sends, or queries, binary test patterns.The BIN command causes the Stereo/RDS Coder to send periodic binary bit patterns instead of RDS data.


## Parameters:
<x>

0

binary mode OFF

1

00000000...,

2

11111111...,

3

01010101...,

4

11001100...

Example:

STEReo:DIRect "BIN=2"

The binary test pattern is set to "2" so that only "1s" are transmit- ted.

Operating Manual 1407.0806.32 ─ 23

467

R&S ® SMB100A

Remote Control Commands

