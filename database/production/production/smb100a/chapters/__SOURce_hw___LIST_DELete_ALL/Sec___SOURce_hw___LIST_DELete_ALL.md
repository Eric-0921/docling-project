# [:SOURce<hw>]:LIST:DELete:ALL
Deletes all lists in the selected directory.

Note: The list mode must be previously disabled to make sure that no records are selected when you set the frequency mode ( [:SOURce<hw>]:FREQuency:MODE ).

The files are stored with the fixed file extensions *.lsw in a directory of the user's choice. You can select the directory with the commands :MMEMory:CDIRectory or [:SOURce<hw>]:LIST:CATalog? .

*RST does not affect data lists.

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

366

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

Example:

MMEM:CDIR '/var/Listmode'

selects the directory for the list mode files.

FREQ:MODE SWE

deactivates the list mode for RF output and activates the sweep mode.

LIST:DEL:ALL

deletes all list mode files in the selected directory.

Usage:

Event

Manual operation:

See "List Mode Data... - List Mode" on page 196

