# 5.5.6 Operation status register (STATus:OPERation)
This condition part contains information on the actions currently being performed by the instrument, while the event part contains information on the actions performed by the instrument since the last readout of the register.

To read the register, use the query commands STAT:OPER:COND? or STAT:OPER[:EVEN]? .

| Bit No.   | Meaning                                                  |
|-----------|----------------------------------------------------------|
| 0         | Calibrating The bit is set during the calibration phase. |
| 1-2       | Not used                                                 |
| 3         |                                                          |
| 4-15      | Not used                                                 |
