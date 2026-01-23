# Clear all the errors in the error queue
    instr.clear_status()
```

Instrument’s status system error queue is clear-on-read. It means, if you query its content, you clear it at the same time. To query and clear list of all the current errors, use the following:

```python