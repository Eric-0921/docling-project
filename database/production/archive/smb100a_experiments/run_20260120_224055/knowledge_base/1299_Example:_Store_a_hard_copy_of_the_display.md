---
chapter_index: 1299
title: "Example:_Store_a_hard_copy_of_the_display"
--- 

# Example:_Store_a_hard_copy_of_the_display

Example: Store a hard copy of the display

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
        //

HCOPy Subsystem

Operating Manual 1407.0806.32 ─ 23

299

R&S ® SMB100A

Remote Control Commands

