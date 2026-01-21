# 4.3.7.4 List Mode
Similar to a sweep, a series of previously defined frequency and level points is processed in List mode. In contrast to a sweep, however, a list with freely selectable value

RF Block

Operating Manual 1407.0806.32 ─ 23

192

R&S ® SMB100A

Instrument Function

RF Block

![Picture](#/pictures/239)

![Picture](#/pictures/240)

pairs (frequency and level) can be created. The value range for frequency and level covers the entire configurable value range of the instrument.

Interactions between List mode and other operating modes or settings

List mode and sweeps can not be activated simultaneously, they deactivate each other.

Activating the list mode instantly disables NRP Level Control. A running list mode blocks "NRP Level Control". It can not be activated

The lists can be created in the "List Editor". Each list is stored in its own file with the predefined file extension *.lsw . The name of the list file can be freely selected. The files are loaded from the "Lists..." file manager. Externally created tables with pairs of frequency and level values can be converted into List files using the import function. The external files must have the file extension *.txt or *.csv . These file formats are provided e.g. by the Microsoft ® Excel program. The separators for table columns and for decimal floating-point numerals can be set. In addition, internally created List data can be exported into ASCII files using the export function.

The necessary hardware settings are calculated the first time a list is processed. With long dwell times, this calculation can be performed while the list is being processed; the entered dwell times are observed. With very short dwell times, calculation of the hardware settings increases the dwell time for the initial processing cycle; the entered value is only observed from the second processing cycle onwards. In this case a message appears to inform the user that there is a deviation between the current and set dwell times. No further calculations are required after the first run through a list. The current dwell times will definitely no longer deviate from the set dwell times.

The list is processed from the beginning to the end of the list (modes "Auto", ("External") "Single", ("External") "Step").

