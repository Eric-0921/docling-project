# ● PTRansition / NTRansition
The two transition register parts define which state transition of the CONDition part (none, 0 to 1, 1 to 0 or both) is stored in the EVENt part.

The Positive-TRansition part acts as a transition filter. When a bit of the CONDition part is changed from 0 to 1, the associated PTR bit decides whether the EVENt bit is set to 1.

-PTR bit =1: the EVENt bit is set.

-PTR bit =0: the EVENt bit is not set.

This part can be written into and read as required. Its contents are not affected by reading.

The Negative-TRansition part also acts as a transition filter. When a bit of the CONDition part is changed from 1 to 0, the associated NTR bit decides whether the EVENt bit is set to 1.

-NTR bit =1: the EVENt bit is set.

-NTR bit =0: the EVENt bit is not set.

This part can be written into and read as required. Its contents are not affected by reading.

