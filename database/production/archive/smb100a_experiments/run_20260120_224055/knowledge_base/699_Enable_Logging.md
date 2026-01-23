---
chapter_index: 699
title: "Enable_Logging"
--- 

# Enable_Logging

Enable Logging

Activates recording of R&S NRP power sensor readings.

If enabled, every value measured by a connected power sensor and indicated in the user interface, is written to a log file. Per measurement the function logs the measured value (2 readings when you work with peak sensors), the sensor type and the measurement time (time stamp).

RF Block

Operating Manual 1407.0806.32 ─ 23

177

R&S ® SMB100A

Instrument Function

RF Block

The function automatically creates the file name SensLog<n>.txt and stores the file in *txt format under /var/user/SensorLogging on the hard disk. You can enable logging for each connected sensor separately. If enabled, one file per sensor is written.

Note: This specific function is intended for measurements with long time intervals, or if there is a risk that the connection to the sensor can be interrupted and you need the data for reconstruction.

The simplified recording function continuously writes the values in the file of the corresponding sensor number, like Sens1Log.txt . When you start a new measurement, the existing data will not be overwritten, but added to the file.

If you use this function, it is recommended that you regularly remove the files from the hard disk, since they require storage capacity.

Remote command:

:SENSe<ch>[:POWer]:LOGGing:STATe on page 327

