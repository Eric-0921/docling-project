# RF level vs. RF output level
If you are working with a downstream instrument, e.g. an attenuator or amplifier, you can enter the related parameter value in the level settings dialog ("Offset").

The generator includes these parameters and displays the result in the "Level" field in the status bar, as if the downstream instrument and the generator were one unit. This displayed level value corresponds to the value at the RF output of the downstream instrument. However, the level provided at the RF output of the signal generator corresponds to the level value set in the "Level/EMF/..." dialog.

The instrument activates the "Level Offset" icon in the status bar, when a level offset is set.

The correlation is as follows:

"Level" (in header) = "RF output level" (Level in menu) + "Level offset" (Offset in menu)

RF Block

Operating Manual 1407.0806.32 ─ 23

146

R&S ® SMB100A

Instrument Function

RF Block

![Picture](#/pictures/188)

The RF output is protected against overloading by an external signal applied to the RF output (see Chapter 4.3.5.7, "Reverse Power Protection", on page 167).

