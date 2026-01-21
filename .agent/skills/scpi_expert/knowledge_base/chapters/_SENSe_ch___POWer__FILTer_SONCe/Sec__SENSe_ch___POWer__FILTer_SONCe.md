# :SENSe<ch>[:POWer]:FILTer:SONCe
The command activates the search for the optimum filter length for the current measurement conditions. The found filter length can be retrieved with com- mand :SENSe:POWer:FILTer:LENGth:USER? . This command is only available for user filter mode ( :SENSe:POWer:FILTer:TYPE USER ).

Example:

SENS:FILT:TYPE USER

selects user filter mode.

SENS:FILT:SONC

activates the search for the optimum filter length.

SENS:FILT:LENG?

returns the found optimum filter length.

Response: 128

Usage:

Event

Manual operation:

See "Auto Once" on page 177

