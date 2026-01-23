---
chapter_index: 590
title: "Limit_-_RF_Level"
--- 

# Limit_-_RF_Level

Limit - RF Level

Sets an upper limit for the RF output power.

You can use it to protect your DUT from damage due to high input power. If you enter an RF level above this value, the instrument limits the output power to this specified value, and generates a warning message.

However, the level indication in the status bar is not affected.

Note: The limit value is always effective, regardless of whether you work with "NRP Power Control" or not.

The value is not affected by an instrument preset ([PRESET] key), *RST and the "Save/Recall" function. It is influenced only by the Factory Preset and the factory value is equal to maximum level.

