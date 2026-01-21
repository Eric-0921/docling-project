# 5.5.2 Structure of a SCPI status register
Each SCPI status register consists of five parts. Each part has a width of 16 bits and has different functions. The individual bits are independent of each other, i.e. each hardware status is assigned a bit number, which is valid for all five parts. Bit 15 (the most significant bit) is set to zero for all parts. Thus, the contents of the register parts can be processed by the controller as positive integers.

![Picture](#/pictures/326)

Operating Manual 1407.0806.32 ─ 23

275

R&S ® SMB100A

Remote Control Basics

