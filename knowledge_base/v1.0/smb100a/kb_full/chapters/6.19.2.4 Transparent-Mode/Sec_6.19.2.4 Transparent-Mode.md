# 6.19.2.4 Transparent-Mode
The transparent mode allows the user to transmit freely definable binary data instead of the standard RDS data. Blocks A to D of the RDS groups are used. This means that standard RDS data will no longer be transmitted when transparent data is set. The binary data will be sent even if it constitutes no valid or meaningful RDS data. The transmission of standard RDS data will not be resumed until the transparent data is deleted.

Transmit the alternating sequences '0123456789ABCDEF' and 'ABCDEF0123456789' instead of the RDS data:

Delete the transparent data and switch back to standard RDS data transmission with:

STEReo:DIRECT  "TRANS=01 2 3 4 5 6 7 8 9 ABCDEF, ABCDEF01 2 3 4 5 6 7 8 9"


STEReo:DIREct "TRANS=0"


Max. 20 different data sequences can be defined.

Operating Manual 1407.0806.32 ─ 23

488

R&S ® SMB100A

Transporting

