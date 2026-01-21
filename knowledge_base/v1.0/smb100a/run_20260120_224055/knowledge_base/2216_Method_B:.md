---
chapter_index: 2216
title: "Method_B:"
--- 

# Method_B:

Method B:

Generate a new alternative frequency list with

STEReo :DIREct  "AF=N, 87 . 6, 9 0 . 2 , 8 7 . 6 , 9 0 . 2".

Set the group sequence, e.g.

STEReo: DIRECT "GS=0A, 14A".

The group sequence must contain group 0A

The alternative frequencies are now transmitted in group 0A.

Add another alternative frequency list with

STEReo::DIRECT "AF=+,88 .6,91..2,8 8 .6,91..2"

The frequency lists are not checked for correctness. For this reason, make sure that the syntax is correct.

A maximum of five AF lists can be generated. For type A lists, max. 25 frequencies per list can be specified, for type B lists, max. 12 frequencies per list.

