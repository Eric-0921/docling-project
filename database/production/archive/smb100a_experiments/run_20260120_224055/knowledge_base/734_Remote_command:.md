---
chapter_index: 734
title: "Remote_command:"
--- 

# Remote_command:

Remote command:

[:SOURce<hw>]:SWEep[:FREQuency]:STEP[:LINear] on page 427

Operating Manual 1407.0806.32 ─ 23

185

R&S ® SMB100A

Instrument Function

RF Block

"Step Log"

The step width is determined logarithmically in %, that means as a constant fraction of the current frequency.

Successive frequencies are calculated as follows:

start_f < stop_f f2 = f1 * (1 + step_log / 100) If f2 > stop_f: f2 is set to stop_f.

start_f > stop_f f2 = f1 / (1 + step_log / 100) If f2 < stop_f: f2 is set to stop_f.

When the shape "Triangle" is set, the frequency values on the slope from stop_f back to start_f are the same as on the slope from start_f to stop_f .

