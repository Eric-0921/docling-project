# :SYSTem:ERRor[:NEXT]?
Queries the error/event queue for the oldest item and removes it from the queue.


## Return values:
<Next>

string

Error/event_number,"Error/event_description>[;Device-depend-

ent info]" Error number and a short description of the error. If the queue is empty, the response is 0,"No error" Positive error numbers are instrument-dependent. Negative error numbers are reserved by the SCPI standard. Volatile errors are reported once, at the time they appear. Identi- already been retrieved from (and hence not any more present in)

cal errors are reported repeatedly only if the original error has the error queue.

Example:

SYST:ERR?

Queries the oldest entry in the error queue.

R e s p o n s e \colon \, 0 \, , \, \i n o \ e r r o r \, ^ { \prime }

No errors have occurred since the error queue was last read out.

Usage:

Query only

Manual operation:

See "History" on page 74

