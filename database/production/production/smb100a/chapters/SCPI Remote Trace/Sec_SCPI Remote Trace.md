# SCPI Remote Trace
The remote trace functionality allows you to trace input and output strings at the remote control interface of the R&S SMB.

A recorded trace (message log) can be evaluated directly in the dialog. Use the highlighting and navigation functions provided in the lower toolbar to locate error messages and messages containing arbitrary search strings. You can also export the message log to a *.csv file and evaluate the file using a suitable program.

To trace and display messages:

In the navigation pane, select "Diagnostics" > "SCPI Remote Trace".

In the toolbar bar of the "SCPI Remote Trace" page, select "live mode" > "on" and "logging" > "on".

"live mode > on" displays all commands and responses, and "logging > on" also traces messages.

Operating Manual 1407.0806.32 ─ 23

46

R&S ® SMB100A

Getting Started

Preparing for Use

If you now control the R&S SMB with SCPI commands, using an appropriate tool, the SCPI remote trace records the information sent and received.

![Picture](#/pictures/38)

The function records all sent commands, received responses and messages, and stores them in an internal database. If "live mode" is disabled, you can display the recent traces upon request, using the "refresh" button. You can also store the log in a file.

Note: The diagnostics functionality is extended in later releases, e.g. to download or upload SCPI command files from / to the instrument.

