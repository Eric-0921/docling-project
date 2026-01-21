# ALC OFF (Sample & Hold)
In "S&H" mode, the signal generator switches for a short period of time into CW mode and activates ALC. ALC adjusts the level to the set value and the generator holds the value (freeze). Then, the generator switches ALC off again and back to the operating mode.

RF output behavior during Sample & Hold depends on the configuration of your instrument. Instruments equipped with...:

an electronic step attenuator The level is decreased by 30 dB.

● a mechanical step attenuator By default, the mechanical step attenuator is not switched during S&H cycles to optimize the settling time. The instrument provides the output power for 3 ... 5 ms. However, you can affect the attenuation at the output by the setting "RF during Power Search" to "Minimum", see RF During Power Search - ALC. Then the generator decreases the level by 30 dB with the mechanical attenuator. Note that this may take a certain period of time. High frequency instruments, such as the R&S SMB with one of the high frequency options R&S SMB-B120 or R&S SMB-B140, are equipped with a mechanical step attenuator.

no step attenuator

The signal generator outputs the set level for 3 to 5 ms after level or frequency setting during a Sample & hold measurement.

Instruments equipped with one of the options R&S SMB-B112L, R&S SMB-B120L or R&S SMB-B140L come without step attenuator.

The level control status is permanently displayed as a status message in the info line.

![Picture](#/pictures/197)

Operating Manual 1407.0806.32 ─ 23

154

R&S ® SMB100A

Instrument Function

![Picture](#/pictures/198)

