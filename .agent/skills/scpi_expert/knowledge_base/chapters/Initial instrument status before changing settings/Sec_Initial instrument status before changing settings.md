# Initial instrument status before changing settings
Manual operation is designed for maximum possible operating convenience. In contrast, the priority of remote control is the "predictability" of the instrument status. Thus, when a command attempts to define incompatible settings, the command is ignored and the instrument status remains unchanged, i.e. other settings are not automatically adapted. Therefore, control programs should always define an initial instrument status (e.g. using the *RST command) and then implement the required settings.

