# Timeout in milliseconds
instr.visa_timeout = 3000
```

After this time, RsInstrument raises an exception. Speaking of exceptions, an important feature of the RsInstrument is **Instrument Status Checking**. Check out the next chapter that describes the error checking in details.

For completion, we mention other string-based `write_xxx()` and `query_xxx()` methods, all in one example. They are convenient extensions providing type-safe float/boolean/integer setting/querying features:

```python
 1"""
 2Basic string write_xxx / query_xxx.
 3"""
 4
 5from RsInstrument import *
 6
 7instr = RsInstrument('TCPIP::192.168.56.101::INSTR', True, True)
 8instr.visa_timeout = 5000
 9instr.instrument_status_checking = True
10instr.write_int('SWEEP:COUNT ', 10)  # sending 'SWEEP:COUNT 10'
11instr.write_bool('SOURCE:RF:OUTPUT:STATE ', True)  # sending 'SOURCE:RF:OUTPUT:STATE ON'
12instr.write_float('SOURCE:RF:FREQUENCY ', 1E9)  # sending 'SOURCE:RF:FREQUENCY 1000000000'
13
14sc = instr.query_int('SWEEP:COUNT?')  # returning integer number sc=10
15out = instr.query_bool('SOURCE:RF:OUTPUT:STATE?')  # returning boolean out=True
16freq = instr.query_float('SOURCE:RF:FREQUENCY?')  # returning float number freq=1E9
17
18# Close the session
19instr.close()
```

Lastly, a method providing basic synchronization: `query_opc()`. It sends **\*OPC?** to your instrument. The instrument waits with the answer until all the tasks it currently has in the execution queue are finished. This way your program waits too, and it is synchronized with actions in the instrument. Remember to have the VISA timeout set to an appropriate value to prevent the timeout exception. Here’s a snippet:

```python
instr.visa_timeout = 3000
instr.write("INIT")
instr.query_opc()
