---
chapter_index: 2150
title: "Parameters_for_setting_and_query:"
--- 

# Parameters_for_setting_and_query:

Parameters for setting and query:

<FFG>

1A | 3A | 5A | 6A | 7A | 8A | 9A | 10A | 11A | 12A | 13A

Determines the free format group.

To transmit the FFGs of the B group, the same commands are used, only the A groups are replaced by the B groups in the group sequence. If B groups are transmitted, block C is overwrit- ten with the PI code.

Example:

STEReo:DIRect "1A=01,0123456789,1FFFFFFFFF"

Fills a queue with the data "0123456789,1FFFFFFFFF". The data is sent in consecutive order in group 1A after group 1A is added to the group sequence (see command "GS", on page 473 ).

Example:

STEReo:DIRect? "1A"

Reads the data of group 1A.

Response: "01,0123456789,1FFFFFFFFF"

STEReo:DIRect "AF=<A>,<Freq#1>,<Freq#2>,

STEReo:DIRect?

"AF<z>"

Defines an alternative frequency list.

Note: A maximum of five AF lists with max. 25 frequencies per list can be created.

