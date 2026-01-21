---
chapter_index: 1765
title: "Example:_Performing_pulse_modulation"
--- 

# Example:_Performing_pulse_modulation

Example: Performing pulse modulation

This example shows a command sequence to perform pulse modulation.

Programming Examples

            Example: Performing pulse modulation
            This example shows a command sequence to perform pulse modulation.


            // ***************
            // Reset the instrument to start from an initial state
            // ***************
            *RST;  *CLS

            // ***************
            // Set the RF signal frequency and level
            // ***************
            SOURCE:FREQUENCY:CW 400000000
            SOURCE:POWER:LEVEL:IMMEDIATE:AMPLITUDE -25

            // ***************
            // Configure the pulse modulation settings
            // ***************
            // Select the internal modulation generator
            SOURCE:PULM:SOURCE INT
            // Set trigorrge mode
            SOURCE:PULM:TRIGGER:MODE AUTO
            // Select .pi, .se, mode
            SOURCE:PULM:MODE DOUB

            // ***************
            // Alternatively configure the pulse modulation settings for
            // external modulation source
            // ***************
            // Select the external modulation source
            SOURCE:PULM:SOURCE EXT
            // Set the polarity of the externally applied modulation signal.
            SOURCE:PULM:POLARITY NORMAL
            // Select the impedance for the external pulse modulation trigger input
            SOURCE:PULM:TRIGGER:EXTERNAL:IMPedance G10K

            // ***************
            // Configure the pulse generator settings
            // ***************
            // Set pulse period



using Manual 1407.0806.32-23

Operating Manual 1407.0806.32 ─ 23

393

R&S ® SMB100A

Remote Control Commands

SOURCE: PULM:PERIOD 10 us
  // Set pulse width
  SOURCE:PULM:WIDTH 8 us
  // Set double pulse width
  SOURCE:PULM:DOUBLE:WIDTH 0.0000012
  // Set double pulse delay
  SOURCE:PULM:DOUBLE:DELAY 0.00000045

  // **********
  // Activate the signal output
  // **********
  SOURCE:PGENerator:OUTPUT:STATE 1
  SOURCE:PULM:STATE 1
  OUTPUT1:STATE 1

SOURce Subsystem

// Set pulse width
        SOURCE:PULM:WIDTH 8 0
        // Set double pulse width
        SOURCE:PULM:DOUBLE:WIDTH 0.0000012
        // Set double pulse delay
        SOURCE:PULM:DOUBLE:DELAY 0.00000045

        // ***************
        // Activate the signal output
        // ***************
        SOURCE:PGENER:OUTPUT:STATE 1
        SOURCE:PULM:STATE 1 OUTPUT:STATE 1
        OUTPUT1:STATE 1

        -Example:  Genera.r1ing a pulse .train signal.
        This example shows a command sequence to create a pulse train signal.


        // ***************
        // Reset the instrument to start from an initial state
        // ***************
        *RST; *CLS

        // ***************
        // Set the RF signal frequency and level
        // ***************
        SOURCE:FREQ:CWAVE:C0000000
        SOURCE:POWER:LEVEL:IMMEDIATE:AMPLitude -25

        // ***************
        // Create a pulse train data list
        // ***************
        // Select the directory
        MEM:CDIR '/var/use/Lists/'
        // Create and/or select the pulse train data file
        SOURCE:PULM:TRAIN:P_FIVE
        // Enter the pulse train data
        SOURCE:PULM:TRAIN:ONTIME 10s,30s,40s,20s,10ns
        SOURCE:PULM:TRAIN:OFFTIME 10s,40s,50s,40ns,30ns
        SOURCE:PULM:TRAIN:RFPetection 10,1,3,10,6

        // ***************
        // Select pulse train mode
        // ***************
        // Select the interal modulation generator and the pulse mode
        SOURCE:PULM:SOURCE:INTERNAL
        SOURCE:PULM:MODE:PTRain

        // ***************
        


using Manual 1407.0806.32 -- 23

Operating Manual 1407.0806.32 ─ 23

394

R&S ® SMB100A

Remote Control Commands

SOURce Subsystem

