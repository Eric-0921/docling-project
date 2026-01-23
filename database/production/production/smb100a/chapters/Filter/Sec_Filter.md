# Filter
Determines the length of the filter used for the measurement. The filter length affects the measurement time directly.

The averaging filter is used to reduce fluctuations in the measured result to the extent desired. Such fluctuations can be caused by inherent noise of the measuring instrument, modulation of the measurement signal or beats from the superposition of adjacent carriers. A more stable display has to be traded off against longer measurements. The measurement result is obtained from a two-stage averaging process.

Note: Longer measurements do not mean that it takes longer to display a new result, but rather that it takes longer for the result to settle when the power changes.

Operating Manual 1407.0806.32 ─ 23

175

R&S ® SMB100A

Instrument Function

RF Block

Measurements are continuously repeated in a predefined time window. The measurement result is obtained by averaging the measured values for the last 2N time windows. The number N is the filter length, the factor of 2 arises because the output signals from the microwave detector to suppress low-frequency noise are chopped at the same rate as the time windows, which means that an independent measured value can only be obtained from two consecutive values. As the filter length is the multiplier for the time window it directly influences the measurement time.

The filter length can be selected automatically or can be manually set to a fixed value. As a preliminary, you should always check if the auto mode is giving satisfactory results because you will always have to adjust an optimal, manual filter-length setting if the power is not constant.

Selection "Fixed Noise" is offered for achieving defined measurement accuracy.

"Auto"

The filter length is automatically selected and adapted to the currently measured value. With very high signals the filter length and therefore the measurement time can be short. With very low signal levels the filter length and therefore the measurement time is increased in order to reduce noise. The used filter length is indicated in the field to the right, see Filter Length.

"User"

"Fixed Noise"

The filter length is set manually.

The filter length is entered in the entry window to the right. As the filter length works as a multiplier for the time window, this results in a constant measurement time.

Note: The time window varies depending on the used sensor. For most sensors it is fixed to 20 ms. For the R&S NRP-Z81 sensor it is 10 us. Therefore, the user filter length for the R&S NRP-Z81 has be about 1000 times larger than the filter length for other sensors in order to achieve the same filtering result.

The Auto Once button can be used to search for the optimum filter length for the current measurement conditions. The found filter length is indicated in the field to the right, see Filter Length.

The averaging factor is selected so that the sensors intrinsic noise (2 standard deviations) does not exceed the specified noise content. The desired noise content is entered in the entry field to the right, see

Noise Content.

To avoid very long settling times when the power is low, the averaging factor can be limited with the Timeout parameter.

