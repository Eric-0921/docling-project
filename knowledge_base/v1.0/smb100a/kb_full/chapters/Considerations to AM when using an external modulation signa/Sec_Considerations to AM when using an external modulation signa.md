# Considerations to AM when using an external modulation signal:
With Mod Ext Coupling > DC, the RF output signal behaves according to:

input signal = 0 V: the RF output amplitude corresponds to the level value set in the R&S SMB

input signal = +1 V: the output level increases up to the maximum value given by the set modulation sensitivity

input signal = -1 V: the output level decreases down to the minimum value given by the set modulation sensitivity

With Mod Ext Coupling > AC, the modulation input signal is internally highpass filtered. Therefore, the DC content of the input signal is removed before it reaches the amplitude modulator.

The [PULSE EXT] connector at the rear of the instrument controls the external pulse modulation. The input shows some hysteresis with threshold levels of 0.5 V/1.5 V. The voltage must not exceed 5 V.

