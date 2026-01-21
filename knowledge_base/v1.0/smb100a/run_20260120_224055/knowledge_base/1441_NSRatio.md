---
chapter_index: 1441
title: "NSRatio"
--- 

# NSRatio

NSRatio

The filter lenghth (averaging factor) is selected so that the sensor's intrinsic noise (2 standard deviations) does not exceed the specified noise content. The desired noise content is entered with command SENSe:FILTer:NSRatio .

To avoid very long settling times when the power is low, the averaging factor can be limited with the Timeout parameter (command SENSe:FILTer:NSRatio:MTIMe ).

*RST:

AUTO

Example:

SENS:FILT:TYPE AUTO

selects automatic filter selection.

Manual operation:

See "Filter" on page 175

