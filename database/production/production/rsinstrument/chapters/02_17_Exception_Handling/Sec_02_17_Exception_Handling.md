# Exception Handling[](#exception-handling "Link to this heading")

The base class for all the exceptions raised by the RsInstrument is `RsInstrException`. Inherited exception classes:

* `ResourceError` raised in the constructor by problems with initiating the instrument, for example wrong or non-existing resource name.
* `StatusException` raised if a command or a query generated error in the instrument’s error queue.
* `TimeoutException` raised if a visa timeout or an opc timeout is reached.

In this example we show usage of all of them:

```python
 1"""
 2How to deal with RsInstrument exceptions.
 3"""
 4
 5from RsInstrument import *
 6
 7RsInstrument.assert_minimum_version('1.102.0')
 8instr = None
 9# Try-catch for initialization. If an error occurs, the ResourceError is raised
10try:
11    instr = RsInstrument('TCPIP::192.168.1.110::hislip0', True, True)
12except ResourceError as e:
13    print(e.args[0])
14    print('Your instrument is probably OFF...')
15    # Exit now, no point of continuing
16    exit(1)
17try:
18    # Dealing with commands that potentially generate instrument errors:
19    # Switching the status checking OFF temporarily.
20    # We use the InstrumentErrorSuppression context-manager that does it for us:
21    with instr.instr_err_suppressor() as supp:
22        instr.write('MY:MISSpelled:COMMand')
23    if supp.get_errors_occurred():
24        print("Errors occurred: ")
25        for err in supp.get_all_errors():
26            print(err)
27
28    # Here for this query we use the reduced VISA timeout to prevent long waiting
29    with instr.instr_err_suppressor(visa_tout_ms=500) as supp:
30        idn = instr.query('*IDaN')
31    if supp.get_errors_occurred():
32        print("Errors occurred: ")
33        for err in supp.get_all_errors():
34            print(err)
35
36except StatusException as e:
37    # Instrument status error
38    print(e.args[0])
39    print('Nothing to see here, moving on...')
40
41except TimeoutException as e:
42    # Timeout error
43    print(e.args[0])
44    print('That took a long time...')
45
46except RsInstrException as e:
47    # RsInstrException is a base class for all the RsInstrument exceptions
48    print(e.args[0])
49    print('Some other RsInstrument error...')
50
51finally:
52    instr.close()
```
