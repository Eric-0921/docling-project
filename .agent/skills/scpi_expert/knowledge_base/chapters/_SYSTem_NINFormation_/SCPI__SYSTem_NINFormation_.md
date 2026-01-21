# :SYSTem:NINFormation?
Queries the oldest information message ("Error History > Level > Info") in the error/ event queue.


## Return values:
<NextInfo>

string

Example:

:SYSTem:NINFormation?

Queries the oldest entry in the info message queue.

Response: 90,"Info;=== Instrument startup... ==="

Information message containing error number 90, that states, that the instrument startup is complete.

Usage:

Query only

