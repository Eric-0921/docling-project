---
chapter_index: 486
title: "●_List_Mode"
--- 

# ●_List_Mode

● List Mode

The RF signal is generated on the basis of a list of predefined frequency and level values. The duration of the individual steps can be predefined.

Instruments connected downstream can be taken into consideration when setting the frequency and level by entering a frequency and/or level offset.

Automatic level control ("ALC") ensures maximum level accuracy.

User-specific lists which contain level correction values for any frequency range ("User Correction") can be created to, for example, compensate the cable attenuation in a test assembly setup.

RF Block

Operating Manual 1407.0806.32 ─ 23

137

R&S ® SMB100A

Instrument Function

RF Block

The R&S SMB generates the RF signal in unmodulated or analog form. The signal generator is equipped therefore with the following sources for analog modulations:

an internal LF generator

an internal pulse generator

the external modulation inputs [MOD EXT] and [PULSE EXT].

An external trigger signal for the sweeps and the LIST mode can be provided at the [INST TRIG] input.

The input [REF IN] is used to input an external instrument reference, and the output [REF OUT] serves as the output of the reference frequency (internal or external).

