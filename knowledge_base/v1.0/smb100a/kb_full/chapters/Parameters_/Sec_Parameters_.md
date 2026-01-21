# Parameters:
<DataNumber>

Max. 20 different data sequences can be defined.

Range:

0  to  13

<DataStream>

16 ASCII coded hexadecimal characters (blocks A to D of the RDS groups)

TRANS=0 deletes all transparent data and switches back to nor- mal RDS data transmission.

Note: 16 characters must be specified for each data sequence. Leading zeros, if any, must also be specified. The data will be transmitted even if it constitutes no meaningful RDS data.

Example:

STEReo:DIRect "TRANS1=0123456789ABCDEF"

The data "0123456789ABCDEF" is sent instead of the RDS data.

Example:

STEReo:DIRect? "TRANS1"

Reads the transparent data.

Response: "0123456789ABCDEF"

