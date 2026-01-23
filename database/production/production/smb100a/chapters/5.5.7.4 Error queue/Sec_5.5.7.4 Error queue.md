# 5.5.7.4 Error queue
Each error state in the instrument leads to an entry in the error queue. The entries of the error queue are detailed plain text error messages that can be looked up in the Error Log or queried via remote control using SYSTem:ERRor[:NEXT]? . Each call of SYSTem:ERRor[:NEXT]? provides one entry from the error queue. If no error messages are stored there any more, the instrument responds with 0, "No error".

The error queue should be queried after every SRQ in the controller program as the entries describe the cause of an error more precisely than the status registers. Especially in the test phase of a controller program the error queue should be queried regu-

Status reporting system

Operating Manual 1407.0806.32 ─ 23

280

R&S ® SMB100A

Remote Control Basics

