---
chapter_index: 2280
title: "FREQ_OFFSET"
--- 

# FREQ_OFFSET

FREQ OFFSET

A frequency offset is set.

Operating Manual 1407.0806.32 ─ 23

499

R&S ® SMB100A

Status Information, Error Messages and Troubleshooting

Status Information

The frequency entered and displayed in the "Frequency" field takes any set frequency offset into consideration, e.g. an offset set for a downstream instrument. This means that with a frequency offset the frequency displayed in the header does not correspond to the frequency at the RF output, but rather to the frequency at the output of the downstream instrument.

This allows the target frequency at the output of a downstream instrument to be entered in the frequency field. The signal generator changes the RF output frequency according to the entered offset.

However, the frequency entered and displayed in the "Frequency/Phase" dialog of the "RF" function block always corresponds to the RF output frequency. Any frequency offset is not taken into consideration.

The correlation is as follows:

Freq in header = RF output frequency (= Freq in dialog) + Freq offset (= Offset in dialog)

