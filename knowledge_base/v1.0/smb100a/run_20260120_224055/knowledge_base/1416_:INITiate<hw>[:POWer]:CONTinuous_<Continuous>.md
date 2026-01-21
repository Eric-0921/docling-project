---
chapter_index: 1416
title: ":INITiate<hw>[:POWer]:CONTinuous_<Continuous>"
--- 

# :INITiate<hw>[:POWer]:CONTinuous_<Continuous>

:INITiate<hw>[:POWer]:CONTinuous <Continuous>

The command switches the local state of the continuous power measurement by the R&S NRP-Zxx power sensors on and off. Switching off the local state enhances the measurement performance during remote control

The remote measurement is triggered by the READ query (command :READ<ch>[: POWer]? on page 322) which also provides the measurement results. The local state is not influenced by this command, measurements results can be retrieved with local state on or off.

