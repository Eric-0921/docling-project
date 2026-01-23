---
chapter_index: 1979
title: ":STATus:QUEStionable:ENABle_<Enable>"
--- 

# :STATus:QUEStionable:ENABle_<Enable>

:STATus:QUEStionable:ENABle <Enable>

Sets the bits of the ENABle part of the STATus:QUEStionable register. The enable part determines which events of the STATus:EVENt part are enabled for the summary bit in the status byte. These events can be used for a service request.

If a bit in the ENABle part is 1, and the correesponding EVENt bit is true, a positive transition occurs in the summary bit. This transition is reportet to the next higher level.

