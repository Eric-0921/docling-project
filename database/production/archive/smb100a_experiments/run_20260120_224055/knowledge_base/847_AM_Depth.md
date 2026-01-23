---
chapter_index: 847
title: "AM_Depth"
--- 

# AM_Depth

AM Depth

Sets the modulation depth in percent.

Note: With two-tone modulation, observe that the set modulation depth applies to both signals and the sum modulation depth is determined by doubling the set modulation depth. This results in overmodulation if the maximal value for modulation depth is exceeded (see data sheet).

For instruments with frequency option 12 GHz or higher, you can additionally select AM Type Exponential. In this case, the generator sets modulation depth in dB (logarithmic).

Modulation is possible both, upwards and downwards. Accordingly, the dynamic range extends for instruments without attenuator from minimum to maximum level. For instruments with attenuator, the dynamic range corresponds to the Fixed Range (PEP) In; these are downwards about 20 dB, and upwards about 5 dB, that means in total about 25 dB around the set level.

Modulation

Operating Manual 1407.0806.32 ─ 23

205

R&S ® SMB100A

Instrument Function

Modulation

Effects of positive/negative modulation depth:

AM Source Int

-positive depth -> downwards modulation

-negative depth -> upwards modulation

AM Source Ext

-positive depth and negative external voltage -> downwards modulation

-positive depth and positive external voltage -> upwards modulation

-negative depth and negative external voltage -> upwards modulation

-negative depth and positive external voltage -> downwards modulation

