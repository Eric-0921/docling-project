---
chapter_index: 1069
title: "Serial_address"
--- 

# Serial_address

Serial address

The used serial address string is:

ASRL[0-9][::INSTR]

Where ASRL[0-9] determines the number of the COM port on the controller side, that has to be used for the serial connection.

Access via a bluetooth device requires the entry of the bluetooth pin in addition (see Chapter 4.2.3.14, "Security", on page 114).

To enable an error-free and correct data transmission, the parameters of the generator and the controller must have the same setting. The serial interface is preset for a baud rate 115200, no parity and one stop bit. The parameters can be manually changed in "Remote Channel Settings" dialog (see Chapter 4.2.3.10, "Remote Channel Settings", on page 109).

