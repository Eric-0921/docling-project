# 4.3.2.1 RF Frequency vs. RF Output Frequency
If you are working with a downstream instrument, e.g. a mixer or a frequency multiplier, you can enter the related parameter value in the frequency settings dialog ("Offset", "Multiplier").

The generator includes these parameters and displays the result in the "Freq" field in the status bar, as if the downstream instrument and the generator were one unit. This displayed frequency corresponds to the value at the RF output of the downstream instrument. However, the frequency provided at the RF output of the signal generator corresponds to the frequency value set in the "Frequency/Phase" dialog.

The instrument activates the "Freq Offset" icon in the status bar, when a frequency offset or multiplication factor is set.

The correlation between the RF frequency, the RF output frequency and the frequency offset is as follows:

"Freq" (in header) = "RF output frequency" (Frequency in dialog) * "Multiplier" factor (Multiplier in dialog) + "Freq offset" (Offset in dialog)

![Picture](#/pictures/172)

Operating Manual 1407.0806.32 ─ 23

138

R&S ® SMB100A

Instrument Function

RF Block

![Picture](#/pictures/173)

If you have the R&S SMB equipped with one of the microwave frequency options R&S SMB-B112, -B120, -B131 or -B140, you can, in addition, operate an R&S SMZxx frequency multiplier.

xx represents the multiplier type that you can use according to the target frequency range.

Note: Instruments with option R&S SMB-B112 only support the R&S SMZ75(M/E) frequency multiplier models.

