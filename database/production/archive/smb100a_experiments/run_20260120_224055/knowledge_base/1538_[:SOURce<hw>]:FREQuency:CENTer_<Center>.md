---
chapter_index: 1538
title: "[:SOURce<hw>]:FREQuency:CENTer_<Center>"
--- 

# [:SOURce<hw>]:FREQuency:CENTer_<Center>

[:SOURce<hw>]:FREQuency:CENTer <Center>

Sets the center frequency of the RF sweep range.

The range is defined by this center frequency and the specified [:SOURce<hw>]: FREQuency:SPAN , according to the formula:

f _ { C E N T e r } - ( f _ { S P A N } / 2 ) \dots f _ { C E N T e r } + ( f _ { S P A N } / 2 )

with:

Operating Manual 1407.0806.32 ─ 23

346

R&S ® SMB100A

Remote Control Commands

f SPAN = f STOP - f STARt

The center frequency directly relates to the span, and the start and stop frequencies. If you change one of these parameters, the center frequency changes accordingly.

f _ { C E N T e r } = ( f _ { S T O P } + f _ { S T A R T } ) / 2

Note: You can select any frequency within the setting range. The range is defined with the parameters [:SOURce<hw>]:FREQuency:STARt and [:SOURce<hw>]: FREQuency:STOP .

A defined offset and the multiplier factor affect the sweep frequency range and therefore all correlated parameters. The set frequencies are only absolute values, if the offset = 0 and the multiplication factor = 1. The multiplier multiplies the frequencies accordingly, and the offset ≠ 0 shifts the frequencies corresponding to the set value.

3 0 0 \, k H z ^ { * } \, f _ { M U L T i p l i r } + f _ { O F F S e t } \dots \, f _ { \max } \, ^ { * } \, f _ { M U L T i p l i r } + f _ { O F F S e t }

