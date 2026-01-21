---
chapter_index: 754
title: "Example:"
--- 

# Example:

Example:

SOUR:SWE:POW:MODE MAN

TRI:PSW:SOUR SING

SOUR:SWE:POW:STEP 0.5

SOUR:POW:MODE SWE

SOUR:POW:MAN -16

The value entered with command SOUR:SWE:POW:STEP sets the step width.

The value entered with command SOUR:POW:MAN has no effect, the command only triggers the next sweep step. However, the value has to be in the currently set sweep range (start to stop). In remote control only a step-by-step sweep from start to stop frequency is possible.

Sets a single sweep cycle. The sweep is triggered by an external trigger signal.

Refer to the description of the rear panel for information about the connectors for external trigger signal input (see Chapter 3.2.2, "Rear Panel Tour", on page 54).

