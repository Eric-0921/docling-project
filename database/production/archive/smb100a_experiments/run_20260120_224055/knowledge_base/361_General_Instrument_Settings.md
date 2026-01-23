---
chapter_index: 361
title: "General_Instrument_Settings"
--- 

# General_Instrument_Settings

General Instrument Settings

Operating Manual 1407.0806.32 ─ 23

110

R&S ® SMB100A

Instrument Function

General Instrument Settings

For more information on this topic, the application note 1GP89: Remote Emulation with the R&S SMB100A RF and Microwave Signal Generator describes in detail how to use this feature.

The selected instrument also defines the identification string that is retrieved with query *IDN? . In addition to the preset values, you can enter a user-defined identification string, for example to provide individual identification for each generator, like 'MY_R&S SMB' (see Mode and IDN String).

As any other parameter, you can additionally change the remote control command set to be emulated via the Language command. However, once you have switched to an emulation, the R&S SMB specific command set is disabled, that means this command is no longer effective. To return, you need to know the corresponding remote control command of the simulated instrument. If you emulate an HP generator for example, the HP command EX returns to the SCPI command set.

To access this dialog, press the [setup] or [menu] key and select "Remote > Instrument Emulations".

InstrumentEmulations

anguage

SCPI

*IDN?/*OPT?Identification

SCPI

AF2023

Mode

Auto

AF2024

IDN String

AF2030

Rohde&Schwarz,SMB100A,1406.6000k02/00000

0,3.1.17.1-03.01.113 beta (Debug)

OPT String

SMB-B5,SMB-B106,SMB-K22, SMB-K23

The "Instrument Emulations" dialog enables you to emulate a remote control command set of several other signal generators.

The remote commands required to remotely configure the emulation settings are described in Chapter 6.15, "SYSTem Subsystem", on page 437.

