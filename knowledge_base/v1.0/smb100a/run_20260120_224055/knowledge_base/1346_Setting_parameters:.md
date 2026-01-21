---
chapter_index: 1346
title: "Setting_parameters:"
--- 

# Setting_parameters:

Setting parameters:

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

