# Universal commands
Universal commands are encoded in the range 10 through 1F hex. They affect all instruments connected to the bus and do not require addressing.

| Command                           | Effect on the instrument                                                                                                                                            |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DCL (Device Clear)                | Aborts the processing of the commands just received and sets the com- mand processing software to a defined initial state. Does not change the instrument settings. |
| IFC (Interface Clear) *)          | Resets the interfaces to the default setting.                                                                                                                       |
| LLO (Local Lockout)               | The "Local" softkey is disabled. Manual operation is no longer available until GTL is executed.                                                                     |
| SPE (Serial Poll Enable)          | Ready for serial poll.                                                                                                                                              |
| SPD (Serial Poll Disable)         | End of serial poll.                                                                                                                                                 |
| PPU (Parallel Poll Unconfig- ure) | End of the parallel-poll state.                                                                                                                                     |
