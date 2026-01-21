# Dwell Time - List Mode
Enters the dwell time. The dwell time determines the duration of a list step in list operating modes "Auto", "Single" and "Extern Single". In these modes a complete list is processed either once or continuously.

In list operating modes "Step" and "Extern Step", the set dwell time does not affect signal generation. In this case, the duration of a list step is determined by the time between two (internal or external) trigger events.

Operating Manual 1407.0806.32 ─ 23

195

R&S ® SMB100A

Instrument Function

![Picture](#/pictures/244)

The "Dwell Time" set by the user is used as the step time of the list mode. The effective net dwell time is shorter, reduced by the setting time. This setting time may be greater than the time specified in the data sheet.

