# :MMEMory:COPY <SourceFile>[,<DestinationFile>]
Copies an existing file to a new file. Instead of just a file, this command can also be used to copy a complete directory together with all its files.


## Setting parameters:
<SourceFile>

string

String containing the path and file name of the source file

<DestinationFile>

string

String containing the path and name of the target file. The path can be relative or absolute.

If <DestinationFile> is not specified, the <SourceFile> is copied to the current directory, queried with the :MMEMory: CDIRectory command.

Note: Existing files with the same name in the destination direc- tory are overwritten without an error message.

Example:

See "Working with Files and Directories" on page 307.

Usage:

Setting only SCPI confirmed

MMEMory subsystem

Operating Manual 1407.0806.32 ─ 23

309

R&S ® SMB100A

Remote Control Commands

Manual operation:

See "Copy " on page 133

:MMEMory:DATA <Filename>, <BinaryBlock>

:MMEMory:DATA? <Filename>

The setting command writes the block data <BinaryBlock> to the file identified by <Filename> .

Set the GPIB-bus terminator to EOI to ensure correct data transfer.

The query command transfers the specified file from the instrument to the GPIB-bus and then on to the controller. It is important to ensure that the intermediate memory on the controller is large enough to take the file. The setting for the GPIB-bus terminator is irrelevant.

Tip: Use this command to read/transfer stored instrument settings or waveforms directly from/to the instrument.


## Parameters:
<BinaryBlock>

#<number><length_entry><data>

# : Hash sign; always comes first in the binary block <number> : the first digit indicates how many digits the subse- quent length entry has

<length_entry> : indicates the number of subsequent bytes <data> : binary block data for the specified length.

For files with a size with more than nine digits (gigabytes), the instrument allows the syntax #(<Length>) , where <Length> is the file size in decimal format.

