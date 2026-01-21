---
chapter_index: 2219
title: "Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&"
--- 

# Direct_Commands_for_the_Stereo-RDS_Coder_Option_R&

Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5

STEReo: DIRECT ? "EON-PI"

The list shows the EON PI codes already used and those remaining for new data sets.

Create an EON data set with

STEReo: DIRECT "EON-PI=1234"

Set the program service (PS) name for the EON data set with STEReo:DIRect "EON-PS=1234,TEST EON"

Set the group sequence, e.g.: STEReo:DIRect "GS=0A,14A"

Group 14A with variants 0 to 3 is now transmitted.

Create a new AF list for the EON:

Using method A

STEReo::DIREct  "EON-AFA=1 2 3 4 , N, 8 7 . 6 , 8 7 . 7 , 8 7 . 8"

Create further AF lists for the EON, using method A:

STEReo::DIREct	"EON-AFA=1 2 3 4 ,+, 8 8 .6 , 8 8 .7 , 8 8 .8"

Read the first AF list of the EON with STEReo:DIRect? "EON-AFA,1234,1"

Create a new AF list for the EON, using method B:

STEReo:DIRect "EON-AFB=1234,N,87.6,87.7,87.8"

where 87.6 = tuned frequency,

87.7 = mapped frequency 1(variant 5),

87.8 = mapped frequency 2 variant 6)

Note: Do not combine methods A and B for generating EON alternative frequency lists.

A maximum of five AF lists can be generated. For type A lists, max. 25 frequencies per list can be specified, for type B lists, max. five frequencies per list.

