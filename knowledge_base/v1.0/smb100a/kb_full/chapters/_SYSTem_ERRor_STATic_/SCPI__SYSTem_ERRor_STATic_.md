# :SYSTem:ERRor:STATic?
Returns a list of all errors existing at the time when the query is started. This list corresponds to the display on the info page under manual control.


## Return values:
Return values:
					<StaticErrors>            string
					Example:                SYSTEM:ERRor:STATIC?
									// -221, "Settings conflict", 153,"Input voltage out of range", ...
									// returns all static errors that are collected in the error queue

				Usage:                Query only

