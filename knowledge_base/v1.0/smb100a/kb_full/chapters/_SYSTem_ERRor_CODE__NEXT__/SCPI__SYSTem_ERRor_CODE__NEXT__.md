# :SYSTem:ERRor:CODE[:NEXT]?
Queries the error number of the oldest entry in the error queue and then deletes it.


## Return values:
<Next>

string

Returns the error number. To retrieve the entire error text, send the command :SYSTem:ERRor:ALL? .

0

"No error", i.e. the error queue is empty

