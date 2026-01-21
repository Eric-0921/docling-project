# 6.19 Direct Commands for the Stereo/RDS Coder Option R&S SMB-B5
The direct command allow to access all functions of the stereo coder option.

Some of the functions are also available via SCPI commands. In this case, it is recommended to use the SCPI commands in order to keep the settings of the R&S SMB and the stereo coder synchronized. Direct command for which a SCPI command is available are marked with 'for documentation reasons only' and the SCPI command is given.

The direct commands are sent to the Stereo/RDS Coder with

[SOURce:]STEReo:DIRect "command string" .

Information is queried with STEReo:DIRect? "command string" .

All parameters are string parameters, this is the reason why all of them have to be sent in qotation marks ( " - characters are part of the full direct command ! ).

Prior to using the stereo coder, the stereo modulation of the R&S SMB has to be switched on with command SOURce:STEReo:STATe ON . The SCPI command SOURce:STEReo:AUDio:FREQuency sets the LF-Generator frequency and command SOURce:STEReo:MMF limits the modulation frequency. These commands have no counterpart in the direct commands.

