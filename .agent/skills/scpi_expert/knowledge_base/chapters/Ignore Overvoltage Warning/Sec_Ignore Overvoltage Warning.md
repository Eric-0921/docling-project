# Ignore Overvoltage Warning
Suppresses warnings the instrument generates when the modulation signal input is overloaded.

This function prevents a warning caused by signals, that generally comply with the specification, but temporarily overload the input, for example due to spikes. The warning is suppressed in the history, and in the error queue.

Note: This setting is not affected by an instrument preset ([preset] key), *rst or the Save/Recall function. Only the factory preset resets (enables) this setting.

Remote command:

[:SOURce<hw>]:INPut:MODext:WIGNore on page 353

