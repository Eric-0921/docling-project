---
chapter_index: 1558
title: "[:SOURce<hw>]:FREQuency:STARt_<Start>"
--- 

# [:SOURce<hw>]:FREQuency:STARt_<Start>

[:SOURce<hw>]:FREQuency:STARt <Start>

Sets the start frequency for the RF sweep.

This parameter relates to the center frequency and span. If you change the frequency, these parameters change accordingly.

f STARt > f STOP is permitted.

f STARt = (f CENTer - f SPAN /2).

Note: A defined offset and the multiplier factor affect the sweep range and therefore all correlated parameters. The set frequencies are only absolute values, if the offset = 0 and the multiplication factor = 1. The multiplier multiplies the frequencies accordingly, and the offset ≠ 0 shifts the frequencies corresponding to the set value.

f _ { S T A R T } \ast f _ { M U L T i p l ier } + f _ { O F F s e t } \dots f _ { S O P } \ast f _ { M U L T i p l ier } + f _ { O F F s e t }

