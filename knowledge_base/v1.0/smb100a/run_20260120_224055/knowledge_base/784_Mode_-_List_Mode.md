---
chapter_index: 784
title: "Mode_-_List_Mode"
--- 

# Mode_-_List_Mode

Mode - List Mode

Selects the cycle mode of the List mode.

"Auto"

Cycle from the beginning to the end of the list with automatic restart at the beginning. If a different mode was activated prior to the Auto mode, the cycle continues from the beginning of the list. The duration of a list step is determined by the set dwell time. Button "Reset" restarts the list at the starting point.

"Single"

Single cycle from the beginning to the end of the list. If "Single" is selected, the cycle is not started immediately. The "Execute Single" button appears under the "Mode" line. The cycle is started with this button. The duration of a list step is determined by the set dwell time. Button "Reset" restarts the list at the starting point.

Mode

Single

Execute Single

RF Block

Operating Manual 1407.0806.32 ─ 23

194

R&S ® SMB100A

Instrument Function

"Step"

"Extern Single"

"Extern Step"

RF Block

Manual, step-by-step processing of the list. Activating "Step" stops the current list and the cursor moves to the value displayed for "Current Index". It is now possible to scroll up and down in the list in discrete steps by varying the index. The duration of a list step is determined by the time between two index entries.

Button "Reset" restarts the list at the starting point.

Single cycle from the beginning to the end of the list as with "Single", but started by an external trigger.

The external trigger signal is input at the BNC connector [INST TRIG].

Button "Reset" restarts the list at the starting point.

Step-by-step cycle using the external trigger signal. Each trigger event starts a single step. The duration of a list step is determined by the time between two trigger events.

The external trigger signal is input at the BNC connector [INST TRIG].

Button "Reset" restarts the list at the starting point.

