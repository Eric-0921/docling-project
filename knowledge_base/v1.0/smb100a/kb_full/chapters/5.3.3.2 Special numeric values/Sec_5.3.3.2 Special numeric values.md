# 5.3.3.2 Special numeric values
The following mnemonics are special numeric values. In the response to a query, the numeric value is provided.

MIN and MAX : denote the minimum (MINimum) and maximum (MAXimum) value.

DEF : denotes a preset value (DEFault) which has been stored in the EPROM. This value conforms to the default setting, as it is called by the *RST command.

Operating Manual 1407.0806.32 ─ 23

266

R&S ® SMB100A

Remote Control Basics

SCPI command structure

![Picture](#/pictures/322)

UP and DOWN : increases or reduces the numeric value by one step. The step width can be specified via an allocated step command for each parameter which can be set via UP and DOWN.

INF and NINF : INFinity and Negative INFinity (NINF) represent the numeric values 9.9E37 or -9.9E37, respectively. INF and NINF are only sent as instrument responses.

NAN : Not A Number (NAN) represents the value 9.91E37. NAN is only sent as an instrument response. This value is not defined. Possible causes are the division of zero by zero, the subtraction of infinite from infinite and the representation of missing values.

