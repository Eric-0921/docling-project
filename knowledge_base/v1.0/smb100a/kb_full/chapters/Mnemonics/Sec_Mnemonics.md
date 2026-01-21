# Mnemonics
A selection of mnemonics with an identical effect exists for several commands. These mnemonics are indicated in the same line; they are separated by a pipe. Only one of these mnemonics needs to be included in the header of the command. The effect of the command is independent of which of the mnemonics is used.

Example:

Definition SENSE:BANDwidth|BWIDth[:RESolution] <numeric_value>

The two following commands with identical meaning can be created:

SENS:BAND:RES 1

SENS:BWID:RES 1

[ ] Mnemonics in square brackets are optional and may be inserted into the header or omitted.

Example: HCOPy[:IMMediate]

HCOP:IMM is equivalent to HCOP

{ } Parameters in curly brackets are optional and can be inserted once or several times, or omitted.

Example: SENSe:LIST:FREQuency <numeric_value>{,<numeric_value>}

The following are valid commands:

SENS:LIST:FREQ 10

SENS:LIST:FREQ 10,20

SENS:LIST:FREQ 10,20,30,40

