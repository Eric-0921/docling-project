# Ignore Level Range Warnings
Suppresses warnings the instrument generates when either the level, or the PEP value are out of range. This function prevents automated measurements from being stopped due to a level warning.

The following warnings are suppressed in both, the history and in the error queue:

PEP value greater than defined upper bound / PEP value less that defined lower bound (fix range)

Level overrange / level underrange

Remote command:

[:SOURce]:POWer:WIGNore on page 386

