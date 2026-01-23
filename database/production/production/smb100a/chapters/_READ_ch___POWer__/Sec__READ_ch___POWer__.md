# :READ<ch>[:POWer]?
The command triggers the measurement with power sensors and provides the power measurement result of the selected power sensor. The value is provided with the unit set with command SENSe:UNIT[:POWer] .

For certain power sensors, e.g. R&S NRP-Z81, two values are returned, first the value for the average level and - separated by a comma - the peak level

Note: The local state is not influenced by this command, measurements results can be retrieved with local state on or off. For long measurement times it is recommended to use a SRQ (MAV bit) for command synchronization.

Suffix:

.

<ch>

1..3

Return values:

<Power>

string

