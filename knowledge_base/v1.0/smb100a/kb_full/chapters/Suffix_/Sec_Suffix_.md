# Suffix:
.

<ch>

Indicates the protection level.

See also Chapter 4.2.3.13, "Protection", on page 113.

Parameters:

<State>

select

*RST:

n.a. (factory preset: 1)

Operating Manual 1407.0806.32 ─ 23

452

R&S ® SMB100A

Remote Control Commands

SYSTem Subsystem

Setting parameters:

<Key>

integer

The respective functions are disabled when the protection level is activated. No password is required for activation of a level. A password must be entered to deactivate the protection level. The password for the first level is 123456.

Example:

// to activate protection level
        SYSTEM:PROTECT1:STATE 1
        // internal adjustments or hostname cannot be changed
        // to unlock protection level 1
        SYSTEM:PROTECT1:STATE 0,123456
        // internal adjustments are accessible



Manual operation:

See "Protection Level/Password" on page 114

