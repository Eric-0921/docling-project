# 5.1.2 Messages
The messages transferred on the data lines are divided into the following categories:

Interface messages Interface messages are transmitted to the instrument on the data lines, with the

attention line being active (LOW). They are used to communicate between the controller and the instrument. Interface messages can only be sent by instruments that have GPIB bus functionality. For details see the sections for the required interface.

Operating Manual 1407.0806.32 ─ 23

241

R&S ® SMB100A

Remote Control Basics

Instrument messages

Instrument messages are employed in the same way for all interfaces, if not indicated otherwise in the description. Structure and syntax of the instrument messages are described in Chapter 5.3, "SCPI command structure", on page 263. A detailed description of all messages available for the instrument is provided in the chapter "Remote Control Commands".

There are different types of instrument messages, depending on the direction they are sent:

-Commands

-Instrument responses

