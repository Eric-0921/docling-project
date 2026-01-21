---
chapter_index: 1348
title: "Parameters_for_setting_and_query:"
--- 

# Parameters_for_setting_and_query:

Parameters for setting and query:

<Filename>

string

String parameter to specify the name of the file.

Example:

MMEMory:DATA '/var/user/test.txt',#15hallo

Writes the block data to the file test.txt .

The digit 1 indicates a length entry of one digit; the digit 5 indi- cate a length of the binary data ( hallo ) in bytes.

MMEMory:DATA? '/var/user/test.txt'

Sends the data of the file test.txt from the instrument to the controller in the form of a binary block.

Response: #15hallo

Usage:

SCPI confirmed

