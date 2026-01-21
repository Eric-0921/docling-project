# 6.10.1 File naming conventions
To enable files in different file systems to be used, the following file naming conventions should be observed.

The file name can be of any length and is case-sensitive, meaning it is distinguished between uppercase and lowercase letters.

The file and the optional file extension are separated by a dot. All letters and numbers are permitted (numbers are, however, not permitted at the beginning of the file name). If possible, special characters should not be used. The use of the slashes "\" and "/" should be avoided since they are used in file paths. A number of names are reserved for the operating system, e.g. CLOCK$ , CON , AUX , COM1...COM4 , LPT1...LPT3 , NUL and PRN .

In the R&S SMB all files in which lists and settings are stored are given a characteristic extension. The extension is separated from the actual file name by a dot (see "Extensions for User Files" on page 89 for an overview of the file types).

The two characters "*" and "?" function as "wildcards", meaning they are used for selecting several files. The "?" character represents exactly one character, while the "*" character represents all characters up to the end of the file name. "*.*" therefore stands for all files in a directory.

When used in conjunction with the commands, the parameter <file_name> is specified as a string parameter with quotation marks. It can contain either the complete path including the drive, only the path and the file name, or only the file name. The file name must include the file extension. The same applies for the parameters <directory_name> and <path> .

MMEMory subsystem

Operating Manual 1407.0806.32 ─ 23

305

R&S ® SMB100A

Remote Control Commands

MMEMory subsystem

Depending on how much information is provided, either the values specified in the parameter or the values specified with the command MMEM:CDIR (default directory) are used for the path and the drive settings in the commands.

Before the instrument settings can be stored in a file, they have to be stored in an intermediate memory using common command *SAV <number> . The specified number is subsequently used in the :MMEMory:STORe:STATe on page 313 command. Also, subsequently to loading a file with instrument settings with command :MMEMory: LOAD:STATe on page 312, these settings have to be activated with the common command *RCL <number> .

