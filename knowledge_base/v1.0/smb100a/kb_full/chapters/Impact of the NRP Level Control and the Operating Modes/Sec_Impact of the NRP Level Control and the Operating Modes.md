# Impact of the NRP Level Control and the Operating Modes
Since the frequency and level of the RF output signal are continuously adjusted during "NRP Level Control", this operating mode interferes those with varying frequency and level values.

The reason is, that the generator regularly transmits the output frequency to the connected R&S NRPxx power sensor, which in turn requests the signal generator to adjust the output level according to its measurement. In contrast to this real time control loop, for example the list operating mode already generates the RF output signal on previously optimized frequency and level value pairs. In this case, the "NRP Level Control" as a second control loop would impact the already determined RF signal values and also considerably slow down the measurement. Similar impacts occur in sweep mode, and also the "NRP Power Viewer" and "NRP Level Control" affect each other's functionality.

Hence, the operating modes exclude each other as follows:

"NRP Level Control" automatically disables NRP Power Viewer, and vice versa.

Activating the RF frequency sweep, RF level sweep or the list mode instantly deactivates a running "NRP Level Control".

A running list or RF sweep mode blocks "NRP Level Control". It can not be activated.

Also keep in mind that modulated signals may differ from CW signals regarding mean power and peak power. This affects the operation of "NRP Level Control".

RF Block

Operating Manual 1407.0806.32 ─ 23

156

R&S ® SMB100A

Instrument Function

RF Block

![Picture](#/pictures/202)

