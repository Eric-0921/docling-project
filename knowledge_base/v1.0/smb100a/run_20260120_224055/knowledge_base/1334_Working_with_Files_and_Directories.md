---
chapter_index: 1334
title: "Working_with_Files_and_Directories"
--- 

# Working_with_Files_and_Directories

Working with Files and Directories

Read out all files in the specified directory.

I:  Read out all lines in the specified double.
            MMEM: CAT? ' /usb/user'

            Response: 127145265,1753251844,"test,DIR,0","temp,DIR,0",
            "readme.txt,ASC,1324","state.savrcltxt,STAT,5327",
            "waveform.wv,RN 2342"

"waveform.wv,BIN,2342"

the directory /usb/user contains the subdirectories test and temp as well as the files readme.txt , state.savrcltxt and waveform.wv which have different file types.

Tip: To query only the subdirectories of the current or specified directory, perform:

MEM: DCAT? ' /usb/user'

Response: 'test', 'temp'

To query only the number of subdirectories in the current or specified directory, perform:

MMEM:DCAT:LENG? '/usb/user'

    Response: 2

To query the number of files in the current or specified directory, perform:

MEM: CAT : LENG?  / usb/user'

Response: 3

Create a new subdirectory for mass memory storage in the specified directory. MMEM:MDIR '/usb/new'

Copy the file state to a new file.

MMEM: COPY  '/var/user/state.savrcltxt', '/usr/new'

Rename the file state .

MMEM:MOVE 'state.savrcltxt','state_new.savrcltxt'

Remove the test directory.

MEM:RDIR '/usb/test'

Operating Manual 1407.0806.32 ─ 23

307

R&S ® SMB100A

Remote Control Commands

