# 6.13.2 SOURce:CORRection subsystem
The output level is corrected in the CORRection subsystem. Correction is performed by user-defined table values being added to the output level for the respective RF frequency. In the R&S SMB, this subsystem is used to select, transfer and activate user correction tables.

Each list is stored as a file. The name of the user correction file can be freely selected. The file extension *.uco is assigned automatically and cannot be changed.

The files can be stored in a freely selectable directory and opened from there. The default directory is set using command :MMEMory:CDIRectory on page 309. In the case of files which are stored in the default directory, only the file name has to be specified in commands. Otherwise, the complete absolute path has to be specified with every command. The extension can be omitted in any case.

In the following command examples, the files are stored in the default directory.

The amplitude can also be linearized automatically by means of a R&S NRP power sensor connected to the generator output signal. With the aid of the command [: SOURce<hw>]:CORRection:CSET:DATA[:SENSor<ch>][:POWer]:SONCe , a list with correction values for external test assemblies can be automatically determined, e.g. for compensating the frequency response of cables. The correction values can be acquired any time irrespective of the modulation settings of the generator.

SOURce Subsystem

Operating Manual 1407.0806.32 ─ 23

334

R&S ® SMB100A

Remote Control Commands

