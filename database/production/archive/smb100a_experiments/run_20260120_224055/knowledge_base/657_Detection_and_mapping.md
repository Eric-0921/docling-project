---
chapter_index: 657
title: "Detection_and_mapping"
--- 

# Detection_and_mapping

Detection and mapping

The R&S SMB automatically detects a connected R&S NRP power sensor and indicates it in the dilaogs "NRP Power Viewer" NRP Power Viewer Settings and NRP Sensor Mapping dialogs. By default, sensors 1 to 4 are assigned to the sensors at the USB connectors, according to their sequence of connection. In the "Sensor Mapping dialog", you can change the mapping.

For device specific information on the connected sensor, see Chapter 4.2.3.4, "NRP Info/Update", on page 101. For information on the scope of your power sensor refer to the manual of your R&S NRP power sensor.

On connection, the R&S SMB immediately starts the measurement of a detected R&S NRP power sensor. If you perform an instrument preset ([Preset] key or *RST ), the R&S SMB stops the measurements. The connection and the mapping of the power sensors remain, the measurements must be restarted.

A sensor continuously measures the average signal power of the selected source, such as an external signal, or the output signal of the signal generator with the RF level used as reference value. The R&S SMB shows the result in the NRP Power Viewer Settings settings dialog, but you can also permanently display the readings in the block diagram.

Further functions of the R&S SMB related to R&S NRP power sensors are:

Acquisition of level correction data, see Chapter 4.3.5.6, "User Correction", on page 159.

The acquired level correction data is used to create and activate lists in which level correction values predefined by the user are freely assigned to RF frequencies. Correction is performed by the user-defined table values being added to the output level for the respective RF frequency.

NRP Level Control, see Chapter 4.3.5.5, "NRP Level Control", on page 155. Note that "NRP Power Viewer" automatically disables "NRP Level Control", and vice versa.

The software version of the connected power sensor can be retrieved by means of the remote control command SENSe<ch>[:POWer]:TYPE? on page 329. Use the Chapter 4.2.3.4, "NRP Info/Update", on page 101 dialog to update the sensor software.

"NRP Power Viewer" automatically disables NRP Level Control, and vice versa.

Operating Manual 1407.0806.32 ─ 23

171

R&S ® SMB100A

Instrument Function

RF Block

