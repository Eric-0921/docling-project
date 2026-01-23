# HCOPy Subsystem
Remote Control Commands
                                        HCPoy Subsystem
                                       
        // response: "hardcopy1607001.bmp"
        ;HCPoy:FILE:AUTO:NUMBER?
        // queries the number in the automatic file name
        // response: "001"
        ;HCPoy:FILE:AUTO?
        // queries the path and file name of the automatically generated file
        // response: "/usb/HCopy/hardcopy1607001.bmp"
                                        300
        ;HCPoy:DATA?
        ;HCPoy:IMAGE:FORMAT.
        ;HCPoy:DEVICE:LANGUAGE.
        ;HCPoy[:EXECute]...
        ;HCPoy[:FILE[:NAME]:
        ;HCPoy[:FILE[:NAME]:AUTO?..
        ;HCPoy[:FILE[:NAME]:AUTO:DIRECTORY..
        ;HCPoy[:FILE[:NAME]:AUTO:DIRECTORY:CLEAR..
        ;HCPoy[:FILE[:NAME]:AUTO:FILE?.
        ;HCPoy[:FILE[:NAME]:AUTO[:FILE]:DAY:STATE..
        ;HCPoy[:FILE[:NAME]:AUTO[:FILE]:MONTH:STATE..
        ;HCPoy[:FILE[:NAME]:AUTO[:FILE]:YEAR:STATE..
        ;HCPoy[:FILE[:NAME]:AUTO[:FILE]:NUMBER?...
        ;HCPoy[:FILE[:NAME]:AUTO[:FILE]:PREFIX..
        ;HCPoy[:FILE[:NAME]:AUTO[:FILE]:PREFIX:STATE..
        ;HCPoy[:FILE[:NAME]:AUTO:STATE..
        ;HCPoy:REGioign..

        ;HCPoy:DATA?
        Transfers the hardcopy data directly as an NByte stream to the remote client.

