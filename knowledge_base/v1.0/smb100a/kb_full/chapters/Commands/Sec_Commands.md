# Commands
Commands (program messages) are messages the controller sends to the instrument. They operate the instrument functions and request information. The commands are subdivided according to two criteria:

According to the effect they have on the instrument:

-Setting commands cause instrument settings such as a reset of the instrument or setting the frequency.

-Queries cause data to be provided for remote control, e.g. for identification of the instrument or polling a parameter value. Queries are formed by directly appending a question mark to the command header.

According to their definition in standards:

-Common commands : their function and syntax are precisely defined in standard IEEE 488.2. They are employed identically on all instruments (if implemented). They refer to functions such as management of the standardized status registers, reset and self-test.

-Instrument control commands refer to functions depending on the features of the instrument such as frequency settings. Many of these commands have also been standardized by the SCPI committee. These commands are marked as "SCPI confirmed" in the command reference chapters. Commands without this SCPI label are instrument-specific; however, their syntax follows SCPI rules as permitted by the standard.

