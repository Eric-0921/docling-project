---
chapter_index: 2176
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

<EMODE>

1 | 2 | 3 | 4 | 5

1

L: signal in left channel only

2

R: signal in right channel only

3

signal of equal frequency and phase in left and right channel

4

signal of equal frequency and opposite phase in left and right channel

5

different, independent signals in left and right channel (5 is not possible if the internal LF generator is selected as source (SRC = LFGen))

Example:

STEReo:DIRect "MODE=1"

Only the signal of the left channel is transmitted.

Example:

STEReo:DIRect? "MODE"

Example:

STEReo:DIRect "MODE=1"

Only the signal of the left channel is transmitted.

Example:

STEReo:DIRect? "MODE"

Response: "1"

STEReo:DIRect "MS=<Flag>" STEReo:DIRect? "MS"

Sets or reads the music/speech flag.

The flag signals whether music or speech is being transmitted.

