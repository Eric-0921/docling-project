# Transferring Big Data with Progress[](#transferring-big-data-with-progress "Link to this heading")

We can agree that it can be annoying using an application that shows no progress for long-lasting operations. The same is true for remote-control programs. Luckily, RsInstrument has this covered. And, this feature is quite universal - not just for big files transfer, but for any data in both directions.

RsInstrument allows you to register a function (programmer’s fancy name is `handler` or `callback`), which is then periodically invoked after transfer of one data chunk. You can define that chunk size, which gives you control over the callback invoke frequency. You can even slow down the transfer speed, if you want to process the data as they arrive (direction instrument -> PC).

To show this in praxis, we are going to use another *University-Professor-Example*: querying the **\*IDN?** with chunk size of 2 bytes and delay of 200ms between each chunk read:

```python
 1"""
 2Event handlers by reading.
 3"""
 4
 5from RsInstrument import *
 6import time
 7
 8
 9def my_transfer_handler(args):
10    """Function called each time a chunk of data is transferred"""
11    # Total size is not always known at the beginning of the transfer
12    total_size = args.total_size if args.total_size is not None else "unknown"
13
14    print(f"Context: '{args.context}{'with opc' if args.opc_sync else ''}', "
15            f"chunk {args.chunk_ix}, "
16            f"transferred {args.transferred_size} bytes, "
17            f"total size {total_size}, "
18            f"direction {'reading' if args.reading else 'writing'}, "
19            f"data '{args.data}'")
20
21    if args.end_of_transfer:
22        print('End of Transfer')
23    time.sleep(0.2)
24
25
26instr = RsInstrument('TCPIP::192.168.56.101::INSTR', True, True)
27
28instr.events.on_read_handler = my_transfer_handler
29# Switch on the data to be included in the event arguments
30# The event arguments args.data will be updated
31instr.events.io_events_include_data = True
32# Set data chunk size to 2 bytes
33instr.data_chunk_size = 2
34instr.query_str('*IDN?')
35# Unregister the event handler
36instr.events.on_read_handler = None
37
38# Close the session
39instr.close()
```

If you start it, you might wonder (or maybe not): why is the `args.total_size = None`? The reason is, in this particular case the RsInstrument does not know the size of the complete response up-front. However, if you use the same mechanism for transfer of a known data size (for example, a file transfer), you get the information about the total size too, and hence you can calculate the progress as:

*progress [pct] = 100 \* args.transferred\_size / args.total\_size*

Snippet of transferring file from PC to instrument, the rest of the code is the same as in the previous example:

```python
instr.events.on_write_handler = my_transfer_handler
instr.events.io_events_include_data = True
instr.data_chunk_size = 1000
instr.send_file_from_pc_to_instrument(
    r'c:\MyCoolTestProgram\my_big_file.bin',
    r'/var/user/my_big_file.bin')