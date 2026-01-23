---
chapter_index: 578
title: "Example:_How_to_set_up_a_closed_loop_power_control"
--- 

# Example:_How_to_set_up_a_closed_loop_power_control

Example: How to set up a closed loop power control

Figure 4-4: Example of a test setup with NRP Level Control

R&S SMB100A Signal

Generator

Amplifier

DUT

Antenna

RF level

input level

Coupler

R&S NRPxX

Power Sensor

power control

target level

S Parameter (optional)

As shown in the example, the sensor measures a proportional power in defined time intervals, derivated from a coupler. It considers optionally given S-parameters and returns the results to the generator. The signal generator compares the measured level with the set value and adjusts its output level accordingly.

This allows you to control the external signal level continuously and reliably reach a constant input level at the DUT in real time.

