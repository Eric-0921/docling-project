# [:SOURce<hw>]:POWer[:LEVel][:IMMediate]:OFFSet <Offset>
Note:

The level offset is also effective for level sweeps!

Specifies the constant level offset of a downstream attenuator/amplifier. If a level offset is entered, the level entered with :POWer no longer corresponds to the RF output level.

The following correlation applies:

POWer = RF output level + POWer:OFFSet .

Entering a level offset does not change the RF output level, but rather the query value of :POWer .

For more information, see "RF level vs. RF output level" on page 146.

Only dB is permitted as the unit here. The linear units (V, W, etc.) are not permitted.

The keywords of this command are largely optional. Therefore, both the long and short form of the command are shown in the example.

