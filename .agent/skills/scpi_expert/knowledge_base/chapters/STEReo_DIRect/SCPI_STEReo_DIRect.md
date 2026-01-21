# STEReo:DIRect
"MASK=<NumbGroups>,<ErrFreeGroups>,<BitMaskBlcA>,<BitMaskBlcB>,<Bit MaskBlcC>,<BitMaskBlcD>"

STEReo:DIRect? "MASK"

Sets a bit mask to generate defined bit errors in the RDS data stream.


## Setting parameters:
<NumbGroups>

Number of groups to be masked.

If <NumbGroups> is set to zero, the RDS groups are continu- ously linked to the error mask.

If <NumbGroups> is set to a value other than zero, this value is decremented after each errored group transmitted. When zero count is reached, no further errored groups are transmitted, and MASK_STATE is set to "0".

Range:

00  to  FF (hexadecimal values)

<ErrFreeGroups>

Number of error-free groups to be inserted after each errored group.

Range:

00  to  FF (hexadecimal values)

Operating Manual 1407.0806.32 ─ 23

474

R&S ® SMB100A

Remote Control Commands

