# Storing and Loading Current Settings
Store the current setting in an intermediate memory with the number 4. This setting can be called using command *RCL and the associated number of the memory, for example *RCL 4 .

*SAV 4

To store the settings in a file in a specific directory, specify the complete path. MMEM:STOR:STAT 4,"/var/user/test.savrcltxt"

Operating Manual 1407.0806.32 ─ 23

306

R&S ® SMB100A

Remote Control Commands

MMEMory subsystem

To store the settings in a file in the default drive, set the default drive and specify only the file name.

Load the file test.savrcltxt in the user directory. MMEM:LOAD:STAT 4,'/var/user/test.savrcltxt'

Activate the instrument setting of the file test.savrcltxt . *RCL 4

MMEM: CDIR ' /var/user/*$AV 4
  MEM: STOR: STAT 4,"test.savrcltxt"


