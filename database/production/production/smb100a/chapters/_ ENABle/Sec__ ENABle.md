# ● ENABle
The ENABle part determines whether the associated EVENt bit contributes to the sum bit (see below). Each bit of the EVENt part is "ANDed" with the associated ENABle bit (symbol '&'). The results of all logical operations of this part are passed on to the sum bit via an "OR" function (symbol '+').

ENABle bit = 0: the associated EVENt bit does not contribute to the sum bit ENABle bit = 1: if the associated EVENt bit is "1", the sum bit is set to "1" as well.

This part can be written into and read by the user as required. Its contents are not affected by reading.

