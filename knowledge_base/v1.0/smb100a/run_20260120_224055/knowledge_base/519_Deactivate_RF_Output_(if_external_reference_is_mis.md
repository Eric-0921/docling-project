---
chapter_index: 519
title: "Deactivate_RF_Output_(if_external_reference_is_mis"
--- 

# Deactivate_RF_Output_(if_external_reference_is_mis

Deactivate RF Output (if external reference is missing)

Turns the RF output off when the external reference signal is selected, but no signal is supplied.

This function prevents that no improper RF signal due to the missing external reference signal is used for measurements. A message indicates that the external signal is missing and the RF output is deactivated.

This setting is not affected by a reset.

Remote command:

[:SOURce]:ROSCillator:EXTernal:RFOFf[:STATe] on page 410

