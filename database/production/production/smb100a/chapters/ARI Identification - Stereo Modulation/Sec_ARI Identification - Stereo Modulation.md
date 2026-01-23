# ARI Identification - Stereo Modulation
Selects the generated identifiers of the ARI signal.

"Off"

Only the 57 kHz subcarrier is generated (Senderkennung). It marks the stations which broadcast traffic programs and enables the receiver to recognize the frequency as being ARI-capable.

"DK"

"BK"

The message identification (Durchsagekennung) is generated in addition (low-frequency 30% AM). It signalizes that a traffic message is currently broadcasted.

The area identification (Bereichskennung) is generated in addition (60% AM). This code is used to identify the geographical region covered by the radio station. The specific code is selected below.

"DK+BK"

The area and message identification are generated in addition.

Remote command:

[:SOURce]:STEReo:ARI:TYPE on page 414

