---
chapter_index: 607
title: "Edit_User_Cor._Data_-_User_Correction"
--- 

# Edit_User_Cor._Data_-_User_Correction

Edit User Cor. Data - User Correction

Calls the editor for editing the selected user correction list.

A list consists of any number of frequency/level value pairs. The currently selected list is displayed.

Each list is saved as a separate file with extension *.uco . The file name and the directory to which the file is saved are user-selectable.

Note: Save list only after filling both columns (frequency and level), otherwise the entries are lost.

EditUser Correction Data

ucor_list1

区

Frequency/Hz

Power/dB

6

5300000.00

5.42

7.

6 300 000.00

4.73

8

7300.000.00

4.15

9

8300000.00

3.72

10

9.300000.00

3.28

Goto

P3

Save

"Frequency /H z"

"Power/dB"

"Goto"

Enters the frequency to which the level correction value applies.

Note: The "Fill

Enters the level correction value to which the specified frequency applies. The values can be entered manually or automatically with the "Fill With Sensor" function (available in the "Edit" sub menu).

Selects row for editing.

GotoFirst

GotoLast

GotoRow.

If Goto row is selected, a window opens for entering the requested row.

gotoline

OK

Cancel

Operating Manual 1407.0806.32 ─ 23

161

R&S ® SMB100A

Instrument Function

"Edit"

"Insert Row"

"Insert Range"

"Fill

"Fill With Sensor"

"Delete Row"

"Delete

Range

Calls a selection of possible actions described below.

Insert a new row before the marked row.

Insert new rows before the marked row. The number of rows to be inserted can be defined in an entry window.

Opens a sub menu for defining a set of list values to be automatically entered in the ucor list (see "Filling the Correction List automatically" on page 164).

Calls the menu to activate the filling of the user correction list with level values acquired by the selected power sensor (see "Filling the

Correction List with Power Sensor Measurement Data" on page 165).

Deletes the marked row.

Allows to delete any number of rows starting with the marked row. The number of rows to be deleted can be defined in an entry window.

"Save"

The list is saved under its current name.

