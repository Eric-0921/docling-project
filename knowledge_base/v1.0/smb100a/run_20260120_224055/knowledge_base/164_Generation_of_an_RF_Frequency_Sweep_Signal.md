---
chapter_index: 164
title: "Generation_of_an_RF_Frequency_Sweep_Signal"
--- 

# Generation_of_an_RF_Frequency_Sweep_Signal

Generation of an RF Frequency Sweep Signal

In the example, an RF frequency sweep is configured. Proceed as follow:

Activate default (preset) state

Press the [PRESET] key to set a defined instrument state.

Operating Manual 1407.0806.32 ─ 23

59

R&S ® SMB100A

Getting Started

Freq

RFOFF

MOD OFF

Level

1.0000000000

GHz

-30.00

wgp

ALC-S&H

Info

ModGen

Modulation

RF

config

config

config

RF

on

on

On

Configure and activate RF frequency sweep.

Turn the rotary knob and select the "RF" block.

RF

config..

On

Press the rotary knob to open the dialog where the RF frequency sweep can be selected.

RF Sweep/List

Frequency

Sweep

Level Sweep

List Mode

Turn the rotary knob and highlight "RF Frequency Sweep

Press the rotary knob to open the "RF Frequency Sweep" dialog.

RF

Frequency

Sweep

口

State

Off

Mode

Auto

StartFreq

100.000000 000

MHz

StopFreq

500.000 000000

MHz

CenterFreq

300.000000000

MHz

Span

400.000000000

MHz

All sweep parameters are default except for the sweep mode. The default settings are not changed.

Turn the rotary knob to select parameter "Mode", press the rotary knob to open the selection list and select "Single".

RF

Frequency

Sweep

State

Off

Mode

Single

Auto

StartFreq

100Single.

Step

Stop Freq

500

Extern Single

ExternStep

Center Freq

300

ExternStart/Stop

Span

400.000000000

MHz

Press the rotary knob to apply the selection. For triggering, the "Execute Single Sweep" and "Reset Sweep" buttons are displayed.

Trying out the Instrument

Operating Manual 1407.0806.32 ─ 23

60

R&S ® SMB100A

Getting Started

Trying out the Instrument

Finally, select "State" and press the rotary knob to switch on the RF frequency sweep.

RFFrequency

Sweep

State

on

Mode

Single

Execute

SingleSweep

ResetSweep

StartFreq

100.000000000

MHz

Press the [DIAGRAM] key to display the complete block diagram.

The "RF" is not yet active, which means that no RF signal is output.

Activate RF signal.

Turn the rotary knob to select the "RF" block.

Press the [RF ON/OFF] key to activate the "RF" signal output.

RF

config

On

Sweep

To indicate the active state, the RF block is displayed in blue. An RF signal with the default frequency and level settings is output, i.e. 1 GHz and -30 dBm. The sweep is not yet active, it must be triggered in the sweep dialog.

Trigger RF frequency sweep

Press the [Winbar] key to switch to the "RF Frequency Sweep" dialog. Turn the rotary knob to select the "Execute Single Sweep" button.

RF Frequency

Sweep

State

On

Mode

Single

ExecuteSingleSweep

ResetSweep

StartFreq

100.000000000

MHz

.

Press the rotary knob to trigger (start) the frequency sweep.

A linear single sweep signal is now present at the RF output, starting at 100 MHz. The sweep is processed in 1 MHz steps with dwell time of 10 ms per step up to the stop frequency of 500 MHz.

The sweep starts at 100 MHz, stops at 500 MHz in 1 MHz steps is output with a dwell time of 10 ms per step.

Operating Manual 1407.0806.32 ─ 23

61

R&S ® SMB100A

Getting Started

