# 5.1.6.1 GPIB interface messages
Interface messages are transmitted to the instrument on the data lines, with the attention line (ATN) being active (LOW). They are used for communication between the controller and the instrument and can only be sent by a computer which has the function of a GPIB bus controller. GPIB interface messages can be further subdivided into:

Universal commands : act on all instruments connected to the GPIB bus without previous addressing

Addressed commands : only act on instruments previously addressed as listeners

