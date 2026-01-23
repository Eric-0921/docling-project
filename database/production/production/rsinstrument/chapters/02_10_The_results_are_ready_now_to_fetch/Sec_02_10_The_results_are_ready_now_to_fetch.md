# The results are ready now to fetch
results = instr.query('FETCH:MEASUREMENT?')
```

You can define the VISA timeout directly in the `query_opc`, which is valid only for that call. Afterwards, the VISA timeout is set to the previous value:

```python
instr.write("INIT")
instr.query_opc(3000)
```

Tip

Wait, there’s more: you can send the **\*OPC?** after each `write_xxx()` automatically:

```python