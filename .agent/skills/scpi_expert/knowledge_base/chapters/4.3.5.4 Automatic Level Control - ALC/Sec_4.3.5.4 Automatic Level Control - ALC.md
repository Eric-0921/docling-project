# 4.3.5.4 Automatic Level Control - ALC
Your signal generator is equipped with an automatic level control unit to obtain best RF level accuracy.

A utomatic L evel C ontrol (ALC) is an adaptive control system to stabilize the RF output level. It continuously monitors the current level and adjusts it to keep a steady state over temperature and time.

ALC is active in almost all applications by default. However, the Pulse Modulation mode excludes ALC, as the control loop would detect incorrect values and result in level deviations.

Also note that ALC may detect incorrect values in multi-transmitter test setups. If multiple generators are coupled, reverse power may affect the ALC readings. Based on incorrect values, ALC would have an impact on the signal to intermodulation ratio.

![Picture](#/pictures/196)

Operating Manual 1407.0806.32 ─ 23

153

R&S ® SMB100A

Instrument Function

RF Block

