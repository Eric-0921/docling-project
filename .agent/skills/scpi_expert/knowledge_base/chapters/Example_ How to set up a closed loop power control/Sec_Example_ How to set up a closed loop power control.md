# Example: How to set up a closed loop power control
![Picture](#/pictures/201)

As shown in the example, the sensor measures a proportional power in defined time intervals, derivated from a coupler. It considers optionally given S-parameters and returns the results to the generator. The signal generator compares the measured level with the set value and adjusts its output level accordingly.

This allows you to control the external signal level continuously and reliably reach a constant input level at the DUT in real time.

