# Logging[](#logging "Link to this heading")

Yes, the logging again. This one is tailored for instrument communication. You will appreciate such handy feature when you troubleshoot your program, or just want to protocol the SCPI communication for your test reports.

What can you do with the logger?

* Write SCPI communication to a stream-like object, for example console or file, or both simultaneously
* Log only errors and skip problem-free parts; this way you avoid going through thousands lines of texts
* Investigate duration of certain operations to optimize your program’s performance
* Log custom messages from your program

The logged information can be sent to these targets (one or multiple):

* **Console**: this is the most straight-forward target, but it mixes up with other program outputs…
* **Stream**: the most universal one, see the examples below.
* **UDP Port**: if you wish to send it to another program, or a universal UDP listener. This option is used for example by our [Instrument Control Pycharm Plugin](https://rsicpycharmplugin.readthedocs.io).
