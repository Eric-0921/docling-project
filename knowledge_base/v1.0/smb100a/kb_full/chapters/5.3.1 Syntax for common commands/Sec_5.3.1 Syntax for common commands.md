# 5.3.1 Syntax for common commands
Common (= instrument-independent) commands consist of a header preceded by an asterisk (*), and possibly one or more parameters.

| *RST   | RESET                | Resets the instrument.                              |
|--------|----------------------|-----------------------------------------------------|
| *ESE   | EVENT STATUS ENABLE  | Sets the bits of the event status enable registers. |
| *ESR?  | EVENT STATUS QUERY   | Queries the contents of the event status register.  |
| *IDN?  | IDENTIFICATION QUERY | Queries the instrument identification string.       |
