---
chapter_index: 570
title: "ALC_OFF_(Sample_&_Hold)"
--- 

# ALC_OFF_(Sample_&_Hold)

ALC OFF (Sample & Hold)

In "S&H" mode, the signal generator switches for a short period of time into CW mode and activates ALC. ALC adjusts the level to the set value and the generator holds the value (freeze). Then, the generator switches ALC off again and back to the operating mode.

RF output behavior during Sample & Hold depends on the configuration of your instrument. Instruments equipped with

an electronic step attenuator The level is decreased by 30 dB.

● a mechanical step attenuator By default, the mechanical step attenuator is not switched during S&H cycles to optimize the settling time. The instrument provides the output power for 3

no step attenuator

The signal generator outputs the set level for 3 to 5 ms after level or frequency setting during a Sample & hold measurement.

Instruments equipped with one of the options R&S SMB-B112L, R&S SMB-B120L or R&S SMB-B140L come without step attenuator.

The level control status is permanently displayed as a status message in the info line.

Operating Manual 1407.0806.32 ─ 23

154

R&S ® SMB100A

Instrument Function

