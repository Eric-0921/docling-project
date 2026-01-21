---
chapter_index: 2282
title: "LEVEL_OFFSET"
--- 

# LEVEL_OFFSET

LEVEL OFFSET

A level offset is set.

The level entered and displayed in the "Level" field takes the offset of any downstream attenuators/amplifiers into consideration by way of calculation. This means that with a level offset the level displayed in the header does not correspond to the level at the RF output, but rather to the level at the output of the downstream instrument.

This allows the target level at the output of downstream instruments to be entered. The signal generator changes the RF output level according to the set offset.

However, the level entered and displayed in the "Level" dialog of the "RF" function block always corresponds to the RF output level. Any level offset is not taken into consideration.

The correlation is as follows:

Level in header = RF output level (= Level in dialog) + Level offset

