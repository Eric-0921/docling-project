# Example: Store a hard copy of the display
The following example lists commands to configure and execute a hard copy to an automatic named file.

Example: Store a hard copy of the display
        The following example lists commands to configure and execute a hard copy to an
        automatic named file.


        //  **************
        // Hard copy setting
        //  **************
        ;HCPoy:DEVICE:LANGUAGE: PNG
        ;HCPoy:FILE:NAME:AUTE:STATE: 1
        // defines the output format
        // sets the instrument to automatically create output f.i.e names

        //  **************
        // Configure hard copy options, set automatic naming rules
        // An automatically generated file name consists of:
        // <Prefix><YYYY><MM><DD><Number>.<Format>
        //  **************
        ;HCPoy:DEVICE:LANGUAGE: BMP
        // defines output format *.bmp
        ;HCPoy:REGION DIALOG
        // selects the region to be copied
        ;HCPoy:FILE:AUTO:DIE: R"usb/HCopy"
        // ... sets ...i.t. directory of automatic named file to "/usb/HCopy"
        ;HCPoy:FILE:NAME:AUTE:FILE:PREFIX:STATE 1
        ;HCPoy:FILE:NAME:AUTE:FILE:PREFIX:"hardcopy"
        ;HCPoy:FILE:NAME:AUTE:FILE:YEAR:STATE 1
        ;HCPoy:FILE:NAME:AUTE:FILE:MONTH:STATE 1
        // uses automatic naming prefix
        // sets automatic naming prefix to "hardcopy"
        // uses automatic naming date parameters year and month

        //  **************
        // Execute and transfer the hard copy
        //  **************
        ;HCPoy:EXECute
        ;HCPoy:DATA
        // generates a hard copy
        // transfers the hard copy to the remote client
        ;HCPoy:FILE:AUTO:FILE?
        // queries the automatic file name



using Manual 1407.0806.32--23


HCOPy Subsystem

Operating Manual 1407.0806.32 ─ 23

299

R&S ® SMB100A

Remote Control Commands

