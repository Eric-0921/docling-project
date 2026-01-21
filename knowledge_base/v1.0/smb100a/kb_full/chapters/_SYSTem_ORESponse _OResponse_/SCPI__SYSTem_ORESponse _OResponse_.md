# :SYSTem:ORESponse <OResponse>
Defines the user defined response string for *OPT .

Note : While working in an emulation mode, the instrument's specific command set is disabled, i.e. the SCPI command SYST:ORES is discarded.


## Parameters:
<OResponse>

string

Example:

SYSTEM:IDENT USER
        // Selects a user-defined identification
        SYSTEM:ORES "Test Option"
        // Defines the OPT string 'test option'
        *OPT?
        // Response: 'test option'


Manual operation:

See "OPT String" on page 112

