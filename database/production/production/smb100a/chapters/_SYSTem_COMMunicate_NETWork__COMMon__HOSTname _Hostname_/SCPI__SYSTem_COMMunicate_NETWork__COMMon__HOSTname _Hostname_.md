# :SYSTem:COMMunicate:NETWork[:COMMon]:HOSTname <Hostname>
Sets the individual host name of the R&S SMB.

Note: it is recommended that you do not change the host name in order to avoid problems with the networdk connection. However, if you change the host name be sure to use an unique name.

The host name is a protected parameter, To change it, first disable protection level 1 with command :SYSTem:PROTect<ch>[:STATe] on page 452.

Parameters:

<Hostname>

string

Example:

SYSTem:PROTect1:STATe OFF,123456

SYSTem:COMMunicate:NETWork:HOSTname 'SIGGEN'

sets the individual computer name of the R&S SMB.

Manual operation:

See "Hostname" on page 105

