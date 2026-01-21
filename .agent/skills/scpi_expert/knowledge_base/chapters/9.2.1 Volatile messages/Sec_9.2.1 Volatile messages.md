# 9.2.1 Volatile messages
Volatile messages report automatic settings in the instrument (e.g. switching off of incompatible types of modulation) or on illegal entries that are not accepted by the instrument (e.g. range violations). They are displayed in the info line on a yellow background. They are displayed on top of status information or permanent messages.

Operating Manual 1407.0806.32 ─ 23

502

R&S ® SMB100A

Status Information, Error Messages and Troubleshooting

![Picture](#/pictures/346)

Device-Specific Error Messages

Volatile messages do not normally demand user actions and disappear automatically after a brief period of time. They are stored in the history, however.

SCPI command: :SYSTem:ERRor:ALL? or :SYSTem:ERRor[:NEXT]?

