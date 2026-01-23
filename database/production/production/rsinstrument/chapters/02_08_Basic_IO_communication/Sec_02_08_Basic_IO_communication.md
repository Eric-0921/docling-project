# Basic I/O communication[](#basic-i-o-communication "Link to this heading")

Now we have opened the session, it’s time to do some work. RsInstrument provides two basic methods for communication:

* `write()` - writing a command without an answer e.g.: **\*RST**
* `query()` - querying your instrument, for example with the **\*IDN?** query

Here, you may ask a question: Where is the `read()` ?
Short answer - you do not need it. Long answer - your instrument never sends unsolicited responses. If you send a set-command, you use `write()`. For a query-command, you use `query()`. So, you really do not need it…

Enough with the theory, let us look at an example. Basic write, and query:

```python
 1"""
 2Basic string write_str / query_str.
 3"""
 4
 5from RsInstrument import *
 6
 7instr = RsInstrument('TCPIP::192.168.56.101::INSTR', True, True)
 8instr.write_str('*RST')
 9response = instr.query_str('*IDN?')
10print(response)
11
12# Close the session
13instr.close()
```

This example is so-called “*University-Professor-Example*” - good to show a principle, but never used in praxis. The previously mentioned commands are already a part of the driver’s API. Here is another example, achieving the same goal:

```python
 1"""
 2Basic string write_str / query_str.
 3"""
 4
 5from RsInstrument import *
 6
 7instr = RsInstrument('TCPIP::192.168.56.101::INSTR', True, True)
 8instr.reset()
 9print(instr.idn_string)
10
11# Close the session
12instr.close()
```

One additional feature we need to mention here: **VISA timeout**. To simplify, VISA timeout plays a role in each `query_xxx()`, where the controller (your PC) has to prevent waiting forever for an answer from your instrument. VISA timeout defines that maximum waiting time. You can set/read it with the `visa_timeout` property:

```python