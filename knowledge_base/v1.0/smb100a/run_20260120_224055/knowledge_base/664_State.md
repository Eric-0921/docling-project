---
chapter_index: 664
title: "State"
--- 

# State

State

Activates/deactivates level measurement by the power sensor.

The local state is set with the INIT command. Switching the local state off enhances the measurement performance.

In remote control, the sensors are set up using the SENSe commands. The remote measurement is triggered by the READ query which also provides the measurement results. The state is not influenced by these commands, measurements results can be retrieved with local State on or off.

The sensor is selected by suffix 1, 2, 3 or 4 in key word SENSe or READ of the command header.

Suffix 1 denotes the sensor connected at the first [USB] interface, and suffix 2, 3 and 4 are assigned to further sensors connected via USB. The suffix is identical to the index which is assigned automatically to each sensor upon connection.

To query the availability of a sensor at a given connector, use the command SENSe<ch>[:POWer]:STATus[:DEVice]? on page 329.

