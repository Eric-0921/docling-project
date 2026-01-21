---
chapter_index: 1413
title: "Return_values:"
--- 

# Return_values:

Return values:

<SensorList>

Each entry contains information on the sensor type, serial num- ber and interface.

The order of the entries does not correspond to the order the sensors are displayed in the "NRP Sensor Mapping" dialog.

Example:

const auto& p0007, auto v = const_string_map<string, std::list<const char>>;
            ::SLIST::LIST?
            // Response:
            // "NRP33SSN-V-900007-USB Legacy","NRP-Z211-900001-USB Legacy",
            // "NRP33SSN-V-900005-USBTCM","NRP33SN-V-900011-LAN"
            // list of automatically detected sensors
            // the list can contain more entries

list of automatically detected sensors; the list can contain more entries

Usage:

Query only

Manual operation:

See "Sensor Mapping List" on page 168

