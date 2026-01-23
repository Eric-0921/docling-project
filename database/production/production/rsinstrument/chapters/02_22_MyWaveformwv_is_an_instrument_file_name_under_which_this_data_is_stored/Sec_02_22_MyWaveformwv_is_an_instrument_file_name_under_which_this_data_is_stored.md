# MyWaveform.wv is an instrument file name under which this data is stored
smw.write_bin_block("SOUR:BB:ARB:WAV:DATA 'MyWaveform.wv',", wform_data)
```

Note

Notice the `write_bin_block()` has two parameters:

* string parameter `cmd` for the SCPI command
* bytes parameter `payload` for the actual data to send
