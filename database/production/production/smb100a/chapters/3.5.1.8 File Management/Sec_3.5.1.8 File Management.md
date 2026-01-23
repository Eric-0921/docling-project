# 3.5.1.8 File Management
The R&S SMB uses files to save all instrument data, i.e. system and user data.

The user data includes saved instrument settings and lists and the user correction.

The files are stored in the internal memory of the instrument or on a USB memory stick. The /var directory can be used to save user-defined data; any subdirectory structure can be created on /var . Some default subdirectories are predefined, but can be changed at any time.

The /opt directory is a protected system drive and therefore unaccessible system directory. The files on this directory contain data that must not be changed. Therefore, this drive should not be accessed, since reconstruction of the system partition will lead to data loss. To prevent inadvertent deletion or overwriting of system files, this drive is not specified in the file menus.

Files can be exchanged either via a memory stick or a connected network. A memory stick is connected to the USB interface and is assigned the var/usb/ drive. In the case of a connected network, all network drives that can be accessed are available. The files are accessed in a "Save/Recall" dialog in the individual menus.

The files are differentiated according to their extensions; each type of file is assigned a specific file content. The extension is usually of no consequence to the user since access to the files occurs in the individual menus where only the relevant type of file is

Operating Manual 1407.0806.32 ─ 23

86

R&S ® SMB100A

Getting Started

Instrument Control

![Picture](#/pictures/122)

![Picture](#/pictures/123)

available. See "Extensions for User Files" on page 89 for an overview of the supported file extensions.

The user data can be roughly divided into the following data types:

Settings

Instrument settings can be saved and loaded. In case of saveing, the current setting is saved to the specified file.

Lists

Lists, e.g. user correction lists, can be loaded. They can be generated either externally or internally. For internal generation, a new list must be created in the "File Select" dialog which will then be edited in the list editor of the individual menu.

