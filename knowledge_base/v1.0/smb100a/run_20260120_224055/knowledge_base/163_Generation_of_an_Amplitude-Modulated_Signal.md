---
chapter_index: 163
title: "Generation_of_an_Amplitude-Modulated_Signal"
--- 

# Generation_of_an_Amplitude-Modulated_Signal

Generation of an Amplitude-Modulated Signal

To generate a simple AM-modulated signal, proceed as follow:

Activate default (preset) state Press the [PRESET] key to set a defined instrument state.

Trying out the Instrument

Operating Manual 1407.0806.32 ─ 23

57

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

Select and activate AM modulation

Turn the rotary knob and select the "Modulation" block.

Modulation

config

On

Press the rotary knob to open the dialog where the modulation can be selected. Different modulation modes are available depending on the options

Note: installed.

Modulation

Amplitude Modulation

Frequency Modulation..

Phase Modulation.

Pulse Modulation..

The "Amplitude Mod

Turn the rotary knob and highlight "Amplitude Mod

Press the rotary knob to open the "Amplitude Modulation" dialog.

Amplitude Modulation

State

Off

AMSource

Int

AMDepth

30.0

%

AMSource=INTernal

LFGenFreq

1.00000

kHz

Turn the rotary knob to select parameter "AM Depth", press the rotary knob to allow editing and enter the preferred AM depth with the aid of the numeric keypad and the unit keys.

Amplitude Modulation

State

Off

AMSource

Int

AMDepth

20

%

AMSource=INTernal

LFGenFreq

1.00000

kHz

Trying out the Instrument

Operating Manual 1407.0806.32 ─ 23

58

R&S ® SMB100A

Getting Started

Trying out the Instrument

Finally, select "State" and press the rotary knob to switch on the AM modulation.

Amplitude Modulation

State

On

AMSource

Int

AMDepth

20.0

%

AMSource=INTernal

LFGenFreq

1.00000

kHz

Press the [DIAGRAM] key to display the complete block diagram.

To indicate the active state, the "Modulation" block is displayed in blue. The "RF" is not yet active, which means that no RF signal is output.

Set frequency and level and activate RF signal

Press the [FREQ] key to activate the editing mode for frequency entry. The "Frequency" entry field in the header section of the display is highlighted.

Freq

RF

OFF

MODON

1.000000

00000

GHz

Enter the frequency using the numeric keypad and terminate the entry by pressing a unit key.

Press the [LEVEL] key and enter the level settings in the same way.

Level

-30.00

dBm

Press the [DIAGRAM] key to display the complete block diagram.

Turn the rotary knob to select the "RF" block.

Press the [RF ON/OFF] key to activate the "RF" block.

The AM modulation signal is now present at the RF output.

Freq

Level

363.00000000

MHz

-11.00

dBm

LfSweep,ALC-S&H

Info

ModGen

Modulation

RF

config.

config

config

RF

On

On

On

Swp

AM

