---
chapter_index: 1734
title: "[:SOURce<hw>]:POWer:MANual_<Manual>"
--- 

# [:SOURce<hw>]:POWer:MANual_<Manual>

[:SOURce<hw>]:POWer:MANual <Manual>

In Sweep mode (:SOUR:POW:MODE SWE ) the command sets the level for the next sweep step in the Step sweep mode ( :SOUR:SWE:POW:MODE MAN ). Here only level values between the settings [:SOUR]:POW:STAR and [:SOUR]:POW:STOP are permitted. Each sweep step is triggered by a separate :SOUR:POW:MAN command.

As with the "Level" value entered in the "RF Level" menu, the OFFSet value is also taken into consideration with this command.

The specified value range is therefore only effective if :SOURce:POWer:OFFSet is set to 0. The value range for other OFFset values can be calculated using the following formula:

Minimum level + OFFSet

