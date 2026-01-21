# Max Modulation Freq- Stereo Modulation
Sets the maximum modulation frequency that may be used.

This parameter is valid/required only when pre-emphasis has been activated and an external modulation source is used.

Pre-emphasis increases the high-frequency portions of the signal in the level before the FM modulator is reached. This can lead to internal overload of the modulator in the case of sinewave signals with full modulation. The MMF parameter is used to reduce the internal full modulation to such an extent that sinewave signals with nominal voltage can be transmitted with low distortion at the stereo input even when pre-emphasis up to the set frequency has been activated. However, this reduces the S/N ratio on the basis of the increase in level by the pre-emphasis (at the MMF that has been set).

In the case of normal modulation signals such as voice or music, this parameter can be left at its default value because the amplitude of the high-frequency portions of these signals normally decreases substantially.

