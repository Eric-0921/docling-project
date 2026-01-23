# 5.5.7.3 Query of an instrument status
Each part of any status register can be read using queries. There are two types of commands:

The common commands *ESR? , *IDN? , *IST? , *STB? query the higher-level registers.

The commands of the STATus system query the SCPI registers ( STATus:QUEStionable ...)

The returned value is always a decimal number that represents the bit pattern of the queried register. This number is evaluated by the controller program.

Queries are usually used after an SRQ in order to obtain more detailed information on the cause of the SRQ.

