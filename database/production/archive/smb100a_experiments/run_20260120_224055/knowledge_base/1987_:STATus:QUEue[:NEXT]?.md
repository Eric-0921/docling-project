---
chapter_index: 1987
title: ":STATus:QUEue[:NEXT]?"
--- 

# :STATus:QUEue[:NEXT]?

:STATus:QUEue[:NEXT]?

Queries the oldest entry in the error queue and then deletes it. Positive error numbers denote device-specific errors, and negative error numbers denote error messages defined by SCPI. If the error queue is empty, 0 ("No error") is returned.

The command is identical to :SYSTem:ERRor[:NEXT]? on page 440.

Operating Manual 1407.0806.32 ─ 23

436

R&S ® SMB100A

Remote Control Commands

Return values:

<Next>

string

Example:

:STATus:QUEue?

queries the oldest entry in the error queue.

Response: 0, 'no error'

no errors have occurred since the error queue was last read out

Usage:

Query only

Manual operation:

See "History" on page 74

