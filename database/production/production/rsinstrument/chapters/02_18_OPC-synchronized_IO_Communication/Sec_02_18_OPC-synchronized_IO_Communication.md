# OPC-synchronized I/O Communication[](#opc-synchronized-i-o-communication "Link to this heading")

Now we are getting to the cool stuff: OPC-synchronized communication. OPC stands for OPeration Completed. The idea is: use one method (write or query), which sends the command, and polls the instrument’s status subsystem until it indicates: **“I’m finished”**. The main advantage is, you can use this mechanism for commands that take several seconds, or minutes to complete, and you are still able to interrupt the process if needed. You can also perform other operations with the instrument in a parallel thread.

Now, you might say: **“This sounds complicated, I’ll never use it”**. That is where the RsInstrument comes in: all the **write/query** methods we learned in the previous chapter have their `_with_opc` siblings. For example: `write()` has `write_with_opc()`. You can use them just like the normal write/query with one difference: They all have an optional parameter `timeout`, where you define the maximum time to wait. If you omit it, it uses a value from `opc_timeout` property.
Important difference between the meaning of `visa_timeout` and `opc_timeout`:

* `visa_timeout` is a VISA IO communication timeout. **It does not play any role in the** `_with_opc()` methods. It only defines timeout for the standard `query_xxx()` methods. We recommend to keep it to maximum of 10000 ms.
* `opc_timeout` is a RsInstrument internal timeout, that serves as a default value to all the `_with_opc()` methods. If you explicitly define it in the method API, it is valid only for that one method call.

That was too much theory… now an example:

```python
 1"""
 2Write / Query with OPC.
 3The SCPI commands syntax is for demonstration only.
 4"""
 5
 6from RsInstrument import *
 7
 8instr = RsInstrument('TCPIP::192.168.56.101::INSTR', True, True)
 9instr.visa_timeout = 3000
10# opc_timeout default value is 10000 ms
11instr.opc_timeout = 20000
12
13# Send Reset command and wait for it to finish
14instr.write_str_with_opc('*RST')
15
16# Initiate the measurement and wait for it to finish, define the timeout 50 secs
17# Notice no changing of the VISA timeout
18instr.write_str_with_opc('INIT', 50000)
19# The results are ready, simple fetch returns the results
20# Waiting here is not necessary
21result1 = instr.query_str('FETCH:MEASUREMENT?')
22
23# READ command starts the measurement, we use query_with_opc to wait for the measurement to finish
24result2 = instr.query_str_with_opc('READ:MEASUREMENT?', 50000)
25
26# Close the session
27instr.close()
```
