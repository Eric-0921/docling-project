---
chapter_index: 1347
title: "Parameters:"
--- 

# Parameters:

Parameters:

<BinaryBlock>

#<number><length_entry><data>

# : Hash sign; always comes first in the binary block <number> : the first digit indicates how many digits the subse- quent length entry has

<length_entry> : indicates the number of subsequent bytes <data> : binary block data for the specified length.

For files with a size with more than nine digits (gigabytes), the instrument allows the syntax #(<Length>) , where <Length> is the file size in decimal format.

