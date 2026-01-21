# Starting a remote control over LAN (using VXI-11)
To set the instrument to remote control, you can use the addressed command &GTR , or send any command from the controller.

Start the R&S VISA Tester and establish the connection to the R&S SMB, see "Configuring the controller" on page 252.

In the R&S VISA "Basics" tab, enter a SCPI command, e.g. "*IDN?" and confirm with "Query".

The instrument is switched to remote control when it receives a command from the controller.

Select "Read" to obtain the instrument response.

![Picture](#/pictures/313)

Tip: If the "Show Log" checkbox is checked R&S VISA displays each VISA function call in the log-view on the left. If you check the "Write Log" checkbox the log-view entry is written to the log file as well. You can operate the log-view in two modes: the "Live Mode" shows only the most recent messages whereas the "View Mode" allows you to scroll the history.

To set, e.g. the frequency, enter SOUR1:FREQ 4 GHz and select "Write". To check the performed setting, SOUR1:FREQ? and select "Read".

Operating Manual 1407.0806.32 ─ 23

255

R&S ® SMB100A

Remote Control Basics

