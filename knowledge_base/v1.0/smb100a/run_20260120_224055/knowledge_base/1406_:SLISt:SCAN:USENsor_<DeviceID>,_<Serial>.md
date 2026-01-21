---
chapter_index: 1406
title: ":SLISt:SCAN:USENsor_<DeviceID>,_<Serial>"
--- 

# :SLISt:SCAN:USENsor_<DeviceID>,_<Serial>

:SLISt:SCAN:USENsor <DeviceID>, <Serial>

Scans for R&S NRP power sensors connected over a USB interface.

Parameters:

<Serial>

integer

Range:

0  to  999999

Setting parameters:

<DeviceID>

String or Integer

Range:

0  to  999999

*RST:

0

Example:

:SLISt:SCAN:USENsor 'NRQ6',101624 //sensor name, serial number

:SLISt:SCAN:USENsor #H15b,101624 //device ID (hexadecimal), serial numbe

:SLISt:SCAN:USENsor 347,101624 //device ID (decimal), serial number

Usage:

Setting only

Manual operation:

See "Add USB Sensor settings" on page 169

