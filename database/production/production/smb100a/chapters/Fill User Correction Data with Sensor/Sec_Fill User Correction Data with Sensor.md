# Fill User Correction Data with Sensor
Enables you to fill the table with correction data acquired by a connected power sensor from Rohde & Schwarz.

"Sensor"

Displays connected sensors for selection.

"List To Fill"

Indicates the used list file.

"Include Zeroing"

RF Block

Performs a zeroing procedure before acquiring the user correction data to improve precision. Since during zeroing no signal may be applied to the sensor, RF is temporarily switched off at the generator. When unchecked, the zeroing procedure is skipped. The RF signal level might be blanked shortly. This setting is recommended if blanking of RF is undesirable or the absence of power at the sensor can not be guaranteed.

"Execute"

Performs automatic filling of the list, provided a sensor is detected and the user correction list contains at least one frequency value.

