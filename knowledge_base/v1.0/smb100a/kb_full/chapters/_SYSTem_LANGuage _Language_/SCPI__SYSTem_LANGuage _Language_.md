# :SYSTem:LANGuage <Language>
Sets the remote control command set.

The instrument can also be remote controlled via the command set of several other generators, for example HP generator. See the Application Note 1GP71 at the download area of the product site on the Internet.

Note : While working in a emulation mode, the instrument's specific command set is disabled, i.e. the SCPI command SYSTem:LANGuage will be discarded.

The return to the SCPI command set of the R&S SMB can only be performed by using the appropriate command of the selected command set. For example, the HP command EX returns to the instrument-specific GPIB command set (selection SYST:LANG 'HPxxxx' ).


## Parameters:
<Language>

string

Example:

SYSTem:LANGuage "SCPI"

sets the SCPI command set.

Manual operation:

See "Language" on page 111

