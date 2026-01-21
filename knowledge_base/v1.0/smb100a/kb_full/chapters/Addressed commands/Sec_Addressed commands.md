# Addressed commands
Addressed commands are encoded in the range 00 through 0F hex. They only affect instruments addressed as listeners.

Operating Manual 1407.0806.32 ─ 23

247

R&S ® SMB100A

Remote Control Basics

Remote Control Interfaces and Protocols

| Command                       | Effect on the instrument                                                                                                                                             |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GET (Group Execute Trigger)   | Triggers a previously active instrument function (e.g. a sweep). The effect of the command is the same as with that of a pulse at the external trigger signal input. |
| GTL (Go to Local)             | Transition to the "local" state (manual control).                                                                                                                    |
| GTR (Go to Remote)            | Transition to the "remote" state (remote control).                                                                                                                   |
| PPC (Parallel Poll Configure) | Configures the instrument for parallel poll.                                                                                                                         |
| SDC (Selected Device Clear)   | Aborts the processing of the commands just received and sets the command processing software to a defined initial state. Does not change the instrument setting.     |
