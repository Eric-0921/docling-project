---
chapter_index: 660
title: "Sensor"
--- 

# Sensor

Sensor

Selects the R&S NRP power sensor for display.

In remote control, the sensors are set up using the SENSe commands. The remote measurement is triggered by the READ query which also provides the measurement results.

The sensor is selected by suffix 1, 2, 3 or 4 in key word SENSe or READ of the command header.

Operating Manual 1407.0806.32 ─ 23

172

R&S ® SMB100A

Instrument Function

RF Block

Suffix 1 denotes the sensor connected at the first [USB] interface, and suffix 2, 3 and 4 are assigned to further sensors connected via USB. The suffix is identical to the index which is assigned automatically to each sensor upon connection.

Note: The software version of the connected power sensor can be retrieved by means of the remote control command SENS:POW:TYPE? .

Use the "Setup >" Chapter 4.2.3.4, "NRP Info/Update", on page 101 dialog to update the sensor software.

