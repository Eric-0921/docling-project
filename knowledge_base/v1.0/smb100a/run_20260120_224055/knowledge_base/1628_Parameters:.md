---
chapter_index: 1628
title: "Parameters:"
--- 

# Parameters:

Parameters:

<Filename>

<ascii_file_name>

Example:

LIST:DEXC:MODE IMP

determines that ASCII files with frequency and level value pairs are imported into list mode lists.

LIST:DEXC:AFIL:EXT TXT

determines the extension *.txt for the query.

LIST:DEXC:AFIL:CAT?

queries the available files with extension *.txt .

Response: 'list1,list2'

the ASCII files list1.txt and list2.txt exist.

LIST:DEXC:AFIL:SEL '/var/list.csv'

selects list.csv for import.

LIST:DEXC:SEL '/var/list_imp'

determines the destination file list_imp .

LIST:DEXC:EXEC

imports the ASCII file data into the list file.

Manual operation:

See "Select ASCII Source / Destination - List Mode" on page 199

