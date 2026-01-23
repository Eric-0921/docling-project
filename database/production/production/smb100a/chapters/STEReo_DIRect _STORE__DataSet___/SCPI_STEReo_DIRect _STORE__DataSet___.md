# STEReo:DIRect "STORE=<DataSet#>"
Stores data in the flash memory. All RDS-specific settings are stored in data set <DataSet#> of the flash memory.


## Setting parameters:
<DataSet#>

Range:

1  to  5

Example:

STEReo:DIRect "STORE=1"

The current settings are stored in data set "1"

Usage:

Setting only

STEReo:DIRect "TA=<State>" STEReo:DIRect? "TA"

(for documentation reasons only)

Sets or reads the traffic announcement flag.

This flag signals whether traffic information is currently being broadcast.

Use the SCPI command [:SOURce]:STEReo:RDS:TRAFfic:ANNouncement[: STATe] instead.


## Setting parameters:
<State>

0 | 1

Example:

STEReo:DIRect "TA=1"

The traffic announcement flag is set to "1".

Example:

STEReo:DIRect? "TA"

Response: "1"

STEReo:DIRect "TP=<State>"

STEReo:DIRect? "TP"

(for documentation reasons only)

Operating Manual 1407.0806.32 ─ 23

484

R&S ® SMB100A

Remote Control Commands

