# Filling the Correction List with Power Sensor Measurement Data
The level correction values for the user correction list can be acquired by means of R&S NRP power sensors. The R&S NRP sensors are connected to either the [SENSOR] connector or to one of the [USB] interfaces. Configuration of the connection is performed in the "Power Sensor" menu (see Chapter 4.3.6.2, "NRP Power Viewer", on page 170). The filling of the user correction list with measurement data is performed in the ucor list editor (see "Edit User Cor. Data - User Correction" on page 161).

In the editor, the frequencies for which the correction values are to be acquired are entered in the frequency column (either manually or by means of the "Fill..." menu).

Do not save the list at this point, because the frequency entries are lost as long as there are no entries for the level column also. In the following these entries are automatically acquired by the connected power sensor.

All level correction values for the given frequency values are measured using the Power Sensor and automatically filled in the selected list after the "Execute" button is pressed. The list is automatically stored and recalled again after filling.

Operating Manual 1407.0806.32 ─ 23

165

R&S ® SMB100A

Instrument Function

![Picture](#/pictures/218)

