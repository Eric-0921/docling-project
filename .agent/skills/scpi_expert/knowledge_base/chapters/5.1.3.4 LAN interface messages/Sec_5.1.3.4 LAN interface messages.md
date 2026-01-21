# 5.1.3.4 LAN interface messages
In the LAN connection, the interface messages are called low-level control messages. These messages can be used to emulate interface messages of the GPIB bus.

| Command   | Long term             | Effect on the instrument                                                                                                                                             |
|-----------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| &ABO      | Abort                 | Aborts processing of the commands just received.                                                                                                                     |
| &DCL      | Device Clear          | Aborts processing of the commands just received and sets the command processing software to a defined initial state. Does not change the instrument setting.         |
| &GTL      | Go to Local           | Transition to the "local" state (manual control). (The instrument automatically returns to remote state when a remote command is sent UNLESS &NREN was sent before.) |
| &GTR      | Go to Remote          | Enables automatic transition from local state to remote state by a subsequent remote command (after &NREN was sent).                                                 |
| &GET      | Group Execute Trigger | Triggers a previously active instrument function (e.g. a sweep). The effect of the command is the same as with that of a pulse at the external trigger signal input. |
| &LLO      | Local Lockout         | Disables transition from remote control to manual control by means of the front panel keys.                                                                          |
| &NREN     | Not Remote Enable     | Disables automatic transition from local state to remote state by a subsequent remote command. (To re-activate automatic transition use &GTR .)                      |
| &POL      | Serial Poll           | Starts a serial poll.                                                                                                                                                |
