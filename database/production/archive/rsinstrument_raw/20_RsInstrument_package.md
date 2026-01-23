# RsInstrument package

> Source: https://rsinstrument.readthedocs.io/en/latest/RsInstrument.html

# RsInstrument package[](#rsinstrument-package "Link to this heading")

## Modules[](#modules "Link to this heading")

## RsInstrument.RsInstrument[](#module-RsInstrument.RsInstrument "Link to this heading")

Root class for remote-controlling instrument with SCPI commands.

*class* RsInstrument(*resource\_name: str*, *id\_query: bool = True*, *reset: bool = False*, *options: str = None*, *direct\_session: object = None*)[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument)[](#RsInstrument.RsInstrument.RsInstrument "Link to this definition")
:   Bases: `object`

    Root class for remote-controlling instrument with SCPI commands.

    Initializes new RsInstrument session.

    Parameters:
    :   * **resource\_name** – VISA resource name, e.g. ‘TCPIP::192.168.2.1::INSTR’
        * **id\_query** – if True, the instrument’s model name is verified against the models supported by the driver and eventually throws an exception
        * **reset** – Resets the instrument (sends [\*](#id1)RST) command and clears its status syb-system
        * **direct\_session** – Another driver object or pyVisa object to reuse the session instead of opening a new session
        * **options** – string tokens alternating the driver settings. More tokens are separated by comma.

    Parameter options tokens examples:
    :   * `Simulate=True` - starts the session in simulation mode. Default: `False`
        * `SelectVisa=socketio` - uses no VISA implementation for socket connections - you do not need any VISA-C installation
        * `SelectVisa=rs` - forces usage of RohdeSchwarz Visa
        * `SelectVisa=ni` - forces usage of National Instruments Visa
        * `Profile = HM8123` - setting profile fitting the specific non-standard instruments. Available values: HM8123, CMQ, ATS, Minimal. Default: `none`
        * `OpenTimeout=5000` - sets timeout used at the session opening. This timeout is only used in waiting for a locked session to be freed. Default: `2000ms`
        * `ExclusiveLock=True` - opens the session with exclusive lock on the VISA level. Default: `False`
        * `QueryInstrumentStatus = False` - same as `driver.utilities.instrument_status_checking = False`. Default: `True`
        * `WriteDelay = 20, ReadDelay = 5` - introduces delay of 20ms before each write and 5ms before each read. Default: `0ms` for both
        * `TerminationCharacter = "\r"` - sets the termination character for reading. Default: `\n` (LineFeed or LF)
        * `AssureWriteWithTermChar = True` - makes sure each command/query is terminated with termination character. Default: Interface dependent
        * `AddTermCharToWriteBinBlock = True` - adds one additional LF to the end of the binary data (some instruments require that). Default: `False`
        * `DataChunkSize = 10E3` - maximum size of one write/read segment. If transferred data is bigger, it is split to more segments. Default: `1E7` bytes
        * `OpcTimeout = 10000` - same as driver.utilities.opc\_timeout = 10000. Default: `30000ms`
        * `VisaTimeout = 5000` - same as driver.utilities.visa\_timeout = 5000. Default: `10000ms`
        * `ViClearExeMode = Disabled` - viClear() execution mode. Default: `execute_on_all`
        * `OpcQueryAfterWrite = True` - same as driver.utilities.opc\_query\_after\_write = True. Default: `False`
        * `OpcWaitMode = OpcQuery` - mode for all the opc-synchronised write/reads. Other modes: StbPolling, StbPollingSlow, StbPollingSuperSlow. Default: `StbPolling`
        * `StbInErrorCheck = False` - if true, the driver checks errors with [\*](#id3)STB? If false, it uses SYST:ERR?. Default: `True`
        * `SkipStatusSystemSettings = False` - some instruments do not support full status system commands. In such case, set this value to True. Default: `False`
        * `SkipClearStatus = True` - set to True for instruments that do not support [\*](#id5)CLS command. Default: `False`
        * `DisableOpcQuery = True` - set to True for instruments that do not support [\*](#id7)OPC? query. Default: `False`
        * `EachCmdAsQuery = True`, set to True, for instruments that always return answer. Default: `false`
        * `CmdIdn = ID?` - defines which SCPI command to use for identification query. Use ‘<none>’ string to skip identification query at the init. Default: `*IDN?`
        * `CmdReset = RT` - defines which SCPI command to use for reset. Default: `*RST`
        * `VxiCapable = false` - you can force a session to a VXI-incapable. Default: <interface-dependent>
        * `Encoding = utf-8` - setting of encoding for strings into bytes and vice versa. Default: `charmap`
        * `OpcSyncQueryMechanism = AlsoCheckMav` - setting of mechanism for OPC-synchronised queries. Default: `OnlyCheckMavErrQueue`
        * `FirstCmds = *CLS` - first command(s) to sent after init. Separated more commands/queries with ‘;;’. Default: [``](#id9)[``](#id11)
        * `EachCmdPrefix = lf` - this prefix is added to the beginning of each command sent to the instrument. Default: [``](#id13)[``](#id15)
        * `EachCmdSuffix = cr` - this suffix is added to the end of each command sent to the instrument. Default: [``](#id17)[``](#id19)
        * `StripStringTrailingWhitespaces = True` - use it to strip white spaces from string query responses. Default: `False`
        * `LoggingMode = On` - sets the logging status right from the start. Possible values: On | Off | Error. Default: `Off`
        * `LoggingName = 'MyDevice'` - sets the name to represent the session in the log entries. Default: `<resource_name>`
        * `LoggingFormat = 'PAD_LEFT12(%START_TIME%) PAD_LEFT25(%DEVICE_NAME%) PAD_LEFT12(%DURATION%) %SCPI_COMMAND%'` - sets the format of the log entries. Default: `PAD_LEFT12(%START_TIME%) PAD_LEFT25(%DEVICE_NAME%) PAD_LEFT12(%DURATION%)  %LOG_STRING_INFO%: %LOG_STRING%`
        * `LogToGlobalTarget = True` - sets the logging target to the class-property previously set with RsInstrument.set\_global\_logging\_target() Default: `False`
        * `LoggingToConsole = True` - immediately starts logging to the console. Default: False
        * `LoggingToUdp = True` - immediately starts logging to the UDP port. Default: False
        * `LoggingUdpPort = 49200` - UDP port to log to. Default: 49200
        * `LoggingRelativeTimeOfFirstEntry = True` - Logging starts with relative time set to the first log entry, which causes the first start time to be ‘00:00:00.000’. Default: False

    add\_instr\_option(*option: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.add_instr_option)[](#RsInstrument.RsInstrument.RsInstrument.add_instr_option "Link to this definition")
    :   Adds new option if not already existing.

    *static* assert\_minimum\_version(*min\_version: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.assert_minimum_version)[](#RsInstrument.RsInstrument.RsInstrument.assert_minimum_version "Link to this definition")
    :   Asserts that the driver version fulfills the minimum required version you have entered.
        This way you make sure your installed driver is of the entered version or newer.

    assign\_lock(*lock: RLock*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.assign_lock)[](#RsInstrument.RsInstrument.RsInstrument.assign_lock "Link to this definition")
    :   Assigns the provided thread lock.

    *property* bin\_float\_numbers\_format*: [BinFloatFormat](#RsInstrument.BinFloatFormat "RsInstrument.Internal.Conversions.BinFloatFormat")*[](#RsInstrument.RsInstrument.RsInstrument.bin_float_numbers_format "Link to this definition")
    :   Sets / returns format of float numbers when transferred as binary data

    *property* bin\_int\_numbers\_format*: [BinIntFormat](#RsInstrument.BinIntFormat "RsInstrument.Internal.Conversions.BinIntFormat")*[](#RsInstrument.RsInstrument.RsInstrument.bin_int_numbers_format "Link to this definition")
    :   Sets / returns format of integer numbers when transferred as binary data

    check\_status() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.check_status)[](#RsInstrument.RsInstrument.RsInstrument.check_status "Link to this definition")
    :   Throws InstrumentStatusException in case of an error in the instrument’s error queue.
        The status checking is performed always, independent of the property ‘instrument\_status\_checking’.
        Also, the property ScpiLogger.log\_status\_check\_ok is ignored, and the Status check is always logged.

    *classmethod* clear\_global\_logging\_relative\_timestamp() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.clear_global_logging_relative_timestamp)[](#RsInstrument.RsInstrument.RsInstrument.clear_global_logging_relative_timestamp "Link to this definition")
    :   Clears the global relative timestamp. After this, all the instances using the global relative timestamp continue logging with the absolute timestamps.

    clear\_lock() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.clear_lock)[](#RsInstrument.RsInstrument.RsInstrument.clear_lock "Link to this definition")
    :   Clears the existing thread lock, making the current session thread-independent from others that might share the current thread lock.

    clear\_status() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.clear_status)[](#RsInstrument.RsInstrument.RsInstrument.clear_status "Link to this definition")
    :   Clears instrument’s status system, the session’s I/O buffers and the instrument’s error queue

    close() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.close)[](#RsInstrument.RsInstrument.RsInstrument.close "Link to this definition")
    :   Closes the active RsInstrument session

    *property* data\_chunk\_size*: int*[](#RsInstrument.RsInstrument.RsInstrument.data_chunk_size "Link to this definition")
    :   Returns max chunk size of one data block.

    *property* driver\_version*: str*[](#RsInstrument.RsInstrument.RsInstrument.driver_version "Link to this definition")
    :   Returns the RsInstrument package version

    *property* encoding*: str*[](#RsInstrument.RsInstrument.RsInstrument.encoding "Link to this definition")
    :   Returns string<=>bytes encoding of the session.

    *property* events*: [Events](events.html#RsInstrument.Fixed_Files.Events.Events "RsInstrument.Fixed_Files.Events.Events")*[](#RsInstrument.RsInstrument.RsInstrument.events "Link to this definition")
    :   Interface for event handlers, see [here](events.html#events)

    file\_exists(*instr\_file: str*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.file_exists)[](#RsInstrument.RsInstrument.RsInstrument.file_exists "Link to this definition")
    :   Returns true, if the instrument file exist.

    *classmethod* from\_existing\_session(*session: object*, *options: str = None*) → [RsInstrument](#RsInstrument.RsInstrument.RsInstrument "RsInstrument.RsInstrument.RsInstrument")[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.from_existing_session)[](#RsInstrument.RsInstrument.RsInstrument.from_existing_session "Link to this definition")
    :   Creates a new RsInstrument object with the entered ‘session’ reused.
        :param session: can be another driver or a direct pyvisa session.
        :param options: string tokens alternating the driver settings. More tokens are separated by comma.

    *property* full\_instrument\_model\_name*: str*[](#RsInstrument.RsInstrument.RsInstrument.full_instrument_model_name "Link to this definition")
    :   Returns the current instrument’s full name e.g. ‘FSW26’

    *classmethod* get\_driver\_version() → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_driver_version)[](#RsInstrument.RsInstrument.RsInstrument.get_driver_version "Link to this definition")
    :   Returns the RsInstrument package version

    get\_file\_size(*instr\_file: str*) → int | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_file_size)[](#RsInstrument.RsInstrument.RsInstrument.get_file_size "Link to this definition")
    :   Return size of the instrument file, or None if the file does not exist.

    *classmethod* get\_global\_logging\_relative\_timestamp() → datetime | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_global_logging_relative_timestamp)[](#RsInstrument.RsInstrument.RsInstrument.get_global_logging_relative_timestamp "Link to this definition")
    :   Returns global common relative timestamp for log entries.

    *classmethod* get\_global\_logging\_target()[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_global_logging_target)[](#RsInstrument.RsInstrument.RsInstrument.get_global_logging_target "Link to this definition")
    :   Returns global common target stream.

    get\_last\_sent\_cmd() → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_last_sent_cmd)[](#RsInstrument.RsInstrument.RsInstrument.get_last_sent_cmd "Link to this definition")
    :   Returns the last commands sent to the instrument. Only works in simulation mode.

    get\_lock() → RLock[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_lock)[](#RsInstrument.RsInstrument.RsInstrument.get_lock "Link to this definition")
    :   Returns the thread lock for the current session.

        By default:

        * If you create a new RsInstrument instance with new VISA session, the session gets a new thread lock. You can assign it to another RsInstrument sessions in order to share one physical instrument with a multi-thread access.
        * If you create a new RsInstrument from an existing session, the thread lock is shared automatically making both instances multi-thread safe.

        You can always assign new thread lock by calling `driver.utilities.assign_lock()`

    get\_session\_handle()[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_session_handle)[](#RsInstrument.RsInstrument.RsInstrument.get_session_handle "Link to this definition")
    :   Returns the underlying pyvisa session

    get\_total\_execution\_time() → timedelta[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_total_execution_time)[](#RsInstrument.RsInstrument.RsInstrument.get_total_execution_time "Link to this definition")
    :   Returns total time spent by the library on communicating with the instrument.
        This time is always shorter than get\_total\_time(), since it does not include gaps between the communication.
        You can reset this counter with reset\_time\_statistics().

    get\_total\_time() → timedelta[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_total_time)[](#RsInstrument.RsInstrument.RsInstrument.get_total_time "Link to this definition")
    :   Returns delta time spent by the library between the get\_total\_time\_startpoint() and now.
        This time is always longer than get\_total\_execution\_time(), since it also includes all other activities besides the communication.
        You can set the total time startpoint to now with reset\_time\_statistics().

    get\_total\_time\_startpoint() → datetime[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_total_time_startpoint)[](#RsInstrument.RsInstrument.RsInstrument.get_total_time_startpoint "Link to this definition")
    :   Returns time from which the execution started.
        This is the value that the get\_total\_time() calculates as its reference.
        Calling the reset\_time\_statistics() sets this time to now.

    go\_to\_local(*mixed\_mode: bool = True*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.go_to_local)[](#RsInstrument.RsInstrument.RsInstrument.go_to_local "Link to this definition")
    :   Puts the instrument into local state.
        By default, the method uses a mechanism to keep the instrument in a mixed mode: remote and local.
        That means, you can remote-control your instrument, and at the same time it still allows manual control.
        Set the mixed\_mode to False, if you want your instrument to go to remote mode as soon as it receives the first remote command.

    go\_to\_remote() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.go_to_remote)[](#RsInstrument.RsInstrument.RsInstrument.go_to_remote "Link to this definition")
    :   Puts the instrument into remote state.

    has\_instr\_option(*options: str | List[str]*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.has_instr_option)[](#RsInstrument.RsInstrument.RsInstrument.has_instr_option "Link to this definition")
    :   Returns true, if the entered options (case-insensitive) matches at least one of the installed options (or-logic).
        You can enter either a string with one option, or more options ‘/’-separated, or more options as a list of strings.
        If K0 is present, all the K-options are reported as present. B-options are not affected by K0.
        Example 1: options=’k23’ returns true, if the instrument has the option ‘K23’.
        Example 2: options=’k23 / K23e’ returns true, if the instrument has either the option ‘K23’ or the option ‘K23E’.
        Example 3: options=[‘k11’,’K22’] returns true, if the instrument has either the option ‘K11’ or the option ‘K22’.

    has\_instr\_option\_k0() → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.has_instr_option_k0)[](#RsInstrument.RsInstrument.RsInstrument.has_instr_option_k0 "Link to this definition")
    :   Returns true, if the instrument has K0 installed.

    has\_instr\_option\_regex(*re\_options: str | List[str]*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.has_instr_option_regex)[](#RsInstrument.RsInstrument.RsInstrument.has_instr_option_regex "Link to this definition")
    :   Returns true, if the entered regex string (case-insensitive) matches at least one of the installed options.
        The match must be complete, not just partial (search).
        You can enter either a string with one option, or more options ‘/’-separated, or more options as a list of strings.
        Example 1: re\_options=’k10.’ returns true, if the instrument contains any option ‘K100’ … up to ‘K109’ .
        Example 2: re\_options=’k10. / k20.\*’ returns true, if the instrument contains any of the options ‘K10x’ or ‘K20xxx’.
        Example 3: re\_options=[‘k10.’, ‘k20.\*’] returns true, if the instrument contains any options ‘K10x’ or ‘K20xxx’.

    *property* idn\_string*: str*[](#RsInstrument.RsInstrument.RsInstrument.idn_string "Link to this definition")
    :   Returns instrument’s identification string - the response on the SCPI command [\*](#id21)IDN?

    instr\_err\_suppressor(*visa\_tout\_ms: int = 0*, *suppress\_only\_codes: int | List[int] = None*) → InstrErrorSuppressor[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.instr_err_suppressor)[](#RsInstrument.RsInstrument.RsInstrument.instr_err_suppressor "Link to this definition")
    :   Returns Context Manager that suppresses the instrument errors.
        Other exceptions types are still raised.
        On entering the context, this class clears all the instrument status errors.
        :param visa\_tout\_ms: VISA Timeout in milliseconds, that is set for this context. Afterward, it is changed back. Default value: do-not-change.
        :param suppress\_only\_codes: You can enter a code or list of codes for errors to be suppressed. Other errors will be reported. Example: If you enter -113 here, only the ‘Undefined Header’ error will be suppressed. Default value: suppress-all-errors.

    *property* instrument\_firmware\_version*: str*[](#RsInstrument.RsInstrument.RsInstrument.instrument_firmware_version "Link to this definition")
    :   Returns instrument’s firmware version

    *property* instrument\_model\_name*: str*[](#RsInstrument.RsInstrument.RsInstrument.instrument_model_name "Link to this definition")
    :   Returns the current instrument’s family name e.g. ‘FSW’

    *property* instrument\_options*: List[str]*[](#RsInstrument.RsInstrument.RsInstrument.instrument_options "Link to this definition")
    :   Returns all the instrument options.
        The options are sorted in the ascending order starting with K-options and continuing with B-options

    *property* instrument\_serial\_number*: str*[](#RsInstrument.RsInstrument.RsInstrument.instrument_serial_number "Link to this definition")
    :   Returns instrument’s serial\_number

    *property* instrument\_status\_checking*: bool*[](#RsInstrument.RsInstrument.RsInstrument.instrument_status_checking "Link to this definition")
    :   Sets / returns Instrument Status Checking.
        When True (default is True), all the driver methods and properties are sending “SYSTem:ERRor?”
        at the end to immediately react on error that might have occurred.
        We recommend keeping the state checking ON all the time. Switch it OFF only in rare cases when you require maximum speed.
        The default state after initializing the session is ON.

    is\_connection\_active() → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.is_connection_active)[](#RsInstrument.RsInstrument.RsInstrument.is_connection_active "Link to this definition")
    :   Returns true, if the VISA connection is active and the communication with the instrument still works.
        WARNING!!! this method queries the session’s VISA Timeout and additionally, queries the [\*](#id23)IDN? from the instrument,
        hence affects the performance of your application when used regularly.

    *static* list\_resources(*expression: str = '?\*::INSTR'*, *visa\_select: str = None*) → List[str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.list_resources)[](#RsInstrument.RsInstrument.RsInstrument.list_resources "Link to this definition")
    :   Finds all the resources defined by the expression.

        * ‘?\*’ - matches all the available instruments
        * ‘USB::?\*’ - matches all the USB instruments
        * ‘TCPIP::192?\*’ - matches all the LAN instruments with the IP address starting with 192

        Parameters:
        :   * **expression** – see the examples in the function
            * **visa\_select** – optional parameter selecting a specific VISA. Examples: [‘@ivi](mailto:'%40ivi)’, [‘@rs](mailto:'%40rs)’

    lock\_resource(*timeout: int*, *requested\_key: str | bytes = None*) → bytes | str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.lock_resource)[](#RsInstrument.RsInstrument.RsInstrument.lock_resource "Link to this definition")
    :   Locks the instrument to prevent it from communicating with other clients.

    *property* logger*: [ScpiLogger](logger.html#RsInstrument.Internal.ScpiLogger.ScpiLogger "RsInstrument.Internal.ScpiLogger.ScpiLogger")*[](#RsInstrument.RsInstrument.RsInstrument.logger "Link to this definition")
    :   Scpi Logger interface, see [here](logger.html#logger)

    *property* manufacturer*: str*[](#RsInstrument.RsInstrument.RsInstrument.manufacturer "Link to this definition")
    :   Returns manufacturer of the instrument

    *property* opc\_query\_after\_write*: bool*[](#RsInstrument.RsInstrument.RsInstrument.opc_query_after_write "Link to this definition")
    :   Sets / returns Instrument [\*](#id25)OPC? query sending after each command write.
        When True, (default is False) the driver sends [\*](#id27)OPC? every time a write command is performed.
        Use this if you want to make sure your sequence is performed command-after-command.

    *property* opc\_sync\_query\_mechanism*: [OpcSyncQueryMechanism](#RsInstrument.OpcSyncQueryMechanism "RsInstrument.Internal.InstrumentSettings.OpcSyncQueryMechanism")*[](#RsInstrument.RsInstrument.RsInstrument.opc_sync_query_mechanism "Link to this definition")
    :   Returns the current setting of the OPC-Sync query mechanism.

    *property* opc\_timeout*: int*[](#RsInstrument.RsInstrument.RsInstrument.opc_timeout "Link to this definition")
    :   Sets / returns timeout in milliseconds for all the operations that use OPC synchronization.

    process\_all\_commands() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.process_all_commands)[](#RsInstrument.RsInstrument.RsInstrument.process_all_commands "Link to this definition")
    :   SCPI command: [\*](#id29)WAI
        Stops further commands processing until all commands sent before [\*](#id31)WAI have been executed.

    query(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query)[](#RsInstrument.RsInstrument.RsInstrument.query "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        This method is an alias to the query\_str() method.

    query\_all\_errors() → List[str] | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_all_errors)[](#RsInstrument.RsInstrument.RsInstrument.query_all_errors "Link to this definition")
    :   Queries and clears all the errors from the instrument’s error queue.
        The method returns list of strings as error messages. If no error is detected, the return value is None.
        The process is: querying ‘SYSTem:ERRor?’ in a loop until the error queue is empty.
        If you want to include the error codes, call the query\_all\_errors\_with\_codes()

    query\_all\_errors\_with\_codes() → List[Tuple[int, str]] | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_all_errors_with_codes)[](#RsInstrument.RsInstrument.RsInstrument.query_all_errors_with_codes "Link to this definition")
    :   Queries and clears all the errors from the instrument’s error queue.
        The method returns list of tuples (code: int, message: str). If no error is detected, the return value is None.
        The process is: querying ‘SYSTem:ERRor?’ in a loop until the error queue is empty.

    query\_bin\_block(*query: str*) → bytes[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_block "Link to this definition")
    :   Queries binary data block to bytes.
        Throws an exception if the returned data was not a binary data.
        Returns <data:bytes>

    query\_bin\_block\_to\_file(*query: str*, *file\_path: str*, *append: bool = False*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block_to_file)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_block_to_file "Link to this definition")
    :   Queries binary data block to the provided file.
        If append is False, any existing file content is discarded.
        If append is True, the new content is added to the end of the existing file, or if the file does not exit, it is created.
        Throws an exception if the returned data was not a binary data.
        Example for transferring a file from Instrument -> PC:
        query = f”MMEM:DATA? ‘{INSTR\_FILE\_PATH}’”.

        Alternatively, use the dedicated methods for this purpose:

        * `send_file_from_pc_to_instrument()`
        * `read_file_from_instrument_to_pc()`

    query\_bin\_block\_to\_file\_with\_opc(*query: str*, *file\_path: str*, *append: bool = False*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block_to_file_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_block_to_file_with_opc "Link to this definition")
    :   Sends a OPC-synced query and writes the returned data to the provided file.
        If append is False, any existing file content is discarded.
        If append is True, the new content is added to the end of the existing file, or if the file does not exit, it is created.
        Throws an exception if the returned data was not a binary data.

    query\_bin\_block\_with\_opc(*query: str*, *timeout: int = None*) → bytes[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_block_with_opc "Link to this definition")
    :   Sends a OPC-synced query and returns binary data block to bytes.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_bin\_or\_ascii\_float\_list(*query: str*) → List[float][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_float_list)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_or_ascii_float_list "Link to this definition")
    :   Queries a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

    query\_bin\_or\_ascii\_float\_list\_with\_opc(*query: str*, *timeout: int = None*) → List[float][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_float_list_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_or_ascii_float_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

        If you do not provide timeout, the method uses current opc\_timeout.

    query\_bin\_or\_ascii\_int\_list(*query: str*) → List[int][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_int_list)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_or_ascii_int_list "Link to this definition")
    :   Queries a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

    query\_bin\_or\_ascii\_int\_list\_with\_opc(*query: str*, *timeout: int = None*) → List[int][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_int_list_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_bin_or_ascii_int_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

        If you do not provide timeout, the method uses current opc\_timeout.

    query\_bool(*query: str*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool)[](#RsInstrument.RsInstrument.RsInstrument.query_bool "Link to this definition")
    :   Sends the query to the instrument and returns the response as boolean.

    query\_bool\_list(*query: str*) → List[bool][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool_list)[](#RsInstrument.RsInstrument.RsInstrument.query_bool_list "Link to this definition")
    :   Sends the string query to the instrument and returns the response as List of booleans,
        where the delimiter is comma (‘,’).
        Blank or empty response is returned as an empty list.

    query\_bool\_list\_with\_opc(*query: str*, *timeout: int = None*) → List[bool][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool_list_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_bool_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads response from the instrument as csv-list of booleans.
        If you do not provide timeout, the method uses current opc\_timeout.
        Blank or empty response is returned as an empty list.

    query\_bool\_with\_opc(*query: str*, *timeout: int = None*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_bool_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as boolean.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_float(*query: str*) → float[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_float)[](#RsInstrument.RsInstrument.RsInstrument.query_float "Link to this definition")
    :   Sends the query to the instrument and returns the response as float.

    query\_float\_with\_opc(*query: str*, *timeout: int = None*) → float[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_float_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_float_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as float.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_int(*query: str*) → int[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_int)[](#RsInstrument.RsInstrument.RsInstrument.query_int "Link to this definition")
    :   Sends the query to the instrument and returns the response as integer.

    query\_int\_with\_opc(*query: str*, *timeout: int = None*) → int[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_int_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_int_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as integer.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_opc(*timeout: int = 0*) → int[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_opc "Link to this definition")
    :   SCPI command: [\*](#id33)OPC?
        Queries the instrument’s OPC bit and hence it waits until the instrument reports operation complete.
        If you define timeout > 0, the VISA timeout is set to that value just for this method call.

    query\_str(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str)[](#RsInstrument.RsInstrument.RsInstrument.query_str "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        This method is an alias to the query() method.

    query\_str\_list(*query: str*, *remove\_blank\_response: bool = False*) → List[str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_list)[](#RsInstrument.RsInstrument.RsInstrument.query_str_list "Link to this definition")
    :   Sends the string query to the instrument and returns the response as List of strings, where the delimiter is comma (‘,’). Each element of the list is trimmed for leading and trailing quotes.

        Meaning of the ‘remove\_blank\_response’:
        :   * False(default): whitespaces-only response is returned as a list with one empty element [‘’].
            * True: whitespaces-only response is returned as an empty list [].

    query\_str\_list\_with\_opc(*query: str*, *timeout: int = None*, *remove\_blank\_response: bool = False*) → List[str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_list_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_str_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads response from the instrument as csv-list.
        :   If you do not provide timeout, the method uses current opc\_timeout.

        Meaning of the ‘remove\_blank\_response’:
        :   * False(default): whitespaces-only response is returned as a list with one empty element [‘’].
            * True: whitespaces-only response is returned as an empty list [].

    query\_str\_stripped(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_stripped)[](#RsInstrument.RsInstrument.RsInstrument.query_str_stripped "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string stripped of the trailing LF and leading/trailing single/double quotes.
        The stripping of the leading/trailing quotes is blocked, if the string contains the quotes in the middle.
        This method is an alias to the query\_stripped() method.

    query\_str\_with\_opc(*query: str*, *timeout: int = None*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_str_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_stripped(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_stripped)[](#RsInstrument.RsInstrument.RsInstrument.query_stripped "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string stripped of the trailing LF and leading/trailing single/double quotes.
        The stripping of the leading/trailing quotes is blocked, if the string contains the quotes in the middle.

    query\_with\_opc(*query: str*, *timeout: int = None*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.query_with_opc "Link to this definition")
    :   This method is an alias to the write\_str\_with\_opc().
        Sends the opc-synced query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        If you do not provide timeout, the method uses current opc\_timeout.

    read\_file\_from\_instrument\_to\_pc(*source\_instr\_file: str*, *target\_pc\_file: str*, *append\_to\_pc\_file: bool = False*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.read_file_from_instrument_to_pc)[](#RsInstrument.RsInstrument.RsInstrument.read_file_from_instrument_to_pc "Link to this definition")
    :   SCPI Command: MMEM:DATA?

        Reads file from instrument to the PC.

        Set the `append_to_pc_file` to True if you want to append the read content to the end of the existing PC file.

    reconnect(*force\_close: bool = False*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.reconnect)[](#RsInstrument.RsInstrument.RsInstrument.reconnect "Link to this definition")
    :   If the connection is not active, the method tries to reconnect to the device.
        If the connection is active, and force\_close is False, the method does nothing.
        If the connection is active, and force\_close is True, the method closes, and opens the session again.
        Returns True, if the reconnection has been performed.

    remove\_instr\_option(*option: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.remove_instr_option)[](#RsInstrument.RsInstrument.RsInstrument.remove_instr_option "Link to this definition")
    :   Removes the option if exists.

    reset(*timeout: int = 0*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.reset)[](#RsInstrument.RsInstrument.RsInstrument.reset "Link to this definition")
    :   SCPI command: [\*](#id35)RST
        Sends [\*](#id37)RST command + calls the clear\_status().
        If you define timeout > 0, the VISA timeout is set to that value just for this method call.

    reset\_time\_statistics() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.reset_time_statistics)[](#RsInstrument.RsInstrument.RsInstrument.reset_time_statistics "Link to this definition")
    :   Resets all execution and total time counters.
        Affects the results of get\_total\_time(), get\_total\_execution\_time() and get\_total\_time\_startpoint()

    *property* resource\_name*: str*[](#RsInstrument.RsInstrument.RsInstrument.resource_name "Link to this definition")
    :   Returns the resource name used in the constructor.

    self\_test(*timeout: int = None*) → Tuple[int, str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.self_test)[](#RsInstrument.RsInstrument.RsInstrument.self_test "Link to this definition")
    :   SCPI command: [\*](#id39)TST?
        Performs instrument’s self-test.
        Returns tuple (code:int, message: str). Code 0 means the self-test passed.
        You can define the custom timeout in milliseconds. If you do not define it, the method uses default self-test timeout (usually 60 secs).

    send\_file\_from\_pc\_to\_instrument(*source\_pc\_file: str*, *target\_instr\_file: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.send_file_from_pc_to_instrument)[](#RsInstrument.RsInstrument.RsInstrument.send_file_from_pc_to_instrument "Link to this definition")
    :   SCPI Command: MMEM:DATA

        Sends file from PC to the instrument.

    *classmethod* set\_global\_logging\_relative\_time\_of\_first\_entry() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_relative_time_of_first_entry)[](#RsInstrument.RsInstrument.RsInstrument.set_global_logging_relative_time_of_first_entry "Link to this definition")
    :   This method sets the global flag, that takes the very first log entry start time of any global instance as a global relative timestamp.
        This means, after this call, the first instance that logs an entry set the relative timestamp for all global target instances,
        and begins with the start timestamp 0:00:00.000

    *classmethod* set\_global\_logging\_relative\_timestamp(*timestamp: datetime*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_relative_timestamp)[](#RsInstrument.RsInstrument.RsInstrument.set_global_logging_relative_timestamp "Link to this definition")
    :   Sets global common relative timestamp for log entries. To use it, call the following: io.logger.set\_relative\_timestamp\_global()

    *classmethod* set\_global\_logging\_relative\_timestamp\_now() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_relative_timestamp_now)[](#RsInstrument.RsInstrument.RsInstrument.set_global_logging_relative_timestamp_now "Link to this definition")
    :   Sets global common relative timestamp for log entries to this moment.
        To use it, call the following: io.logger.set\_relative\_timestamp\_global().

    *classmethod* set\_global\_logging\_target(*target*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_target)[](#RsInstrument.RsInstrument.RsInstrument.set_global_logging_target "Link to this definition")
    :   Sets global common target stream that each instance can use. To use it, call the following: io.logger.set\_logging\_target\_global().
        If an instance uses global logging target, it automatically uses the global relative timestamp (if set).
        You can set the target to None to invalidate it.

    *property* supported\_models*: List[str]*[](#RsInstrument.RsInstrument.RsInstrument.supported_models "Link to this definition")
    :   Returns a list of the instrument models supported by this instrument driver

    unlock\_resource() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.unlock_resource)[](#RsInstrument.RsInstrument.RsInstrument.unlock_resource "Link to this definition")
    :   Unlocks the instrument to other clients.

    *property* visa\_manufacturer*: str*[](#RsInstrument.RsInstrument.RsInstrument.visa_manufacturer "Link to this definition")
    :   Returns the manufacturer of the current VISA session.

    *property* visa\_timeout*: int*[](#RsInstrument.RsInstrument.RsInstrument.visa_timeout "Link to this definition")
    :   Sets / returns visa IO timeout in milliseconds.

    visa\_tout\_suppressor(*visa\_tout\_ms: int = 0*) → VisaTimeoutSuppressor[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.visa_tout_suppressor)[](#RsInstrument.RsInstrument.RsInstrument.visa_tout_suppressor "Link to this definition")
    :   Returns Context Manager that suppresses the VISA timeout error.
        Careful!!!: Only the very first VISA Timeout exception is suppressed,
        and afterward the context ends. Therefore, use only one command per context manager,
        if you do not want to skip the following ones.
        :param visa\_tout\_ms: VISA Timeout in milliseconds, that is set for this context. Afterward, it is changed back. Default value: do-not-change.

    write(*cmd: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write)[](#RsInstrument.RsInstrument.RsInstrument.write "Link to this definition")
    :   Writes the command to the instrument as string.
        This method is an alias to the write\_str() method.

    write\_bin\_block(*cmd: str*, *payload: bytes*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bin_block)[](#RsInstrument.RsInstrument.RsInstrument.write_bin_block "Link to this definition")
    :   Writes all the payload as binary data block to the instrument.
        The binary data header is added at the beginning of the transmission automatically, do not include it in the payload!!!

    write\_bin\_block\_from\_file(*cmd: str*, *file\_path: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bin_block_from_file)[](#RsInstrument.RsInstrument.RsInstrument.write_bin_block_from_file "Link to this definition")
    :   Writes data from the file as binary data block to the instrument using the provided command.
        Example for transferring a file from PC -> Instrument:
        cmd = f”MMEM:DATA ‘{INSTR\_FILE\_PATH}’,”.

        Alternatively, use the dedicated methods for this purpose:

        * `send_file_from_pc_to_instrument()`
        * `read_file_from_instrument_to_pc()`

    write\_bool(*cmd: str*, *param: bool*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bool)[](#RsInstrument.RsInstrument.RsInstrument.write_bool "Link to this definition")
    :   Writes the command to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘OUTPUT’ param = ‘True’, result command = ‘OUTPUT ON’

    write\_bool\_with\_opc(*cmd: str*, *param: bool*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bool_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.write_bool_with_opc "Link to this definition")
    :   Writes the command with OPC to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘OUTPUT’ param = ‘True’, result command = ‘OUTPUT ON’
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_float(*cmd: str*, *param: float*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_float)[](#RsInstrument.RsInstrument.RsInstrument.write_float "Link to this definition")
    :   Writes the command to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘CENTER:FREQ’ param = ‘10E6’, result command = ‘CENTER:FREQ 10E6’

    write\_float\_with\_opc(*cmd: str*, *param: float*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_float_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.write_float_with_opc "Link to this definition")
    :   Writes the command with OPC to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘CENTER:FREQ’ param = ‘10E6’, result command = ‘CENTER:FREQ 10E6’
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_int(*cmd: str*, *param: int*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_int)[](#RsInstrument.RsInstrument.RsInstrument.write_int "Link to this definition")
    :   Writes the command to the instrument followed by the integer parameter:
        e.g.: cmd = ‘SELECT:INPUT’ param = ‘2’, result command = ‘SELECT:INPUT 2’

    write\_int\_with\_opc(*cmd: str*, *param: int*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_int_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.write_int_with_opc "Link to this definition")
    :   Writes the command with OPC to the instrument followed by the integer parameter:
        e.g.: cmd = ‘SELECT:INPUT’ param = ‘2’, result command = ‘SELECT:INPUT 2’
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_str(*cmd: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_str)[](#RsInstrument.RsInstrument.RsInstrument.write_str "Link to this definition")
    :   Writes the command to the instrument as string.
        This method is an alias to write() method.

    write\_str\_with\_opc(*cmd: str*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_str_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.write_str_with_opc "Link to this definition")
    :   Writes the opc-synced command to the instrument.
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_with\_opc(*cmd: str*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_with_opc)[](#RsInstrument.RsInstrument.RsInstrument.write_with_opc "Link to this definition")
    :   This method is an alias to the write\_str\_with\_opc().
        Writes the opc-synced command to the instrument.
        If you do not provide timeout, the method uses current opc\_timeout.

## Module contents[](#module-RsInstrument "Link to this heading")

VISA communication interface for SCPI-based instrument remote control.
:version: 1.122.0
:copyright: 2025 by Rohde & Schwarz GMBH & Co. KG
:license: MIT, see LICENSE for more details.

*class* BinFloatFormat(*value*)[[source]](_modules/RsInstrument/Internal/Conversions.html#BinFloatFormat)[](#RsInstrument.BinFloatFormat "Link to this definition")
:   Bases: `Enum`

    Binary format of a float number.

    Double\_8bytes *= 3*[](#RsInstrument.BinFloatFormat.Double_8bytes "Link to this definition")

    Double\_8bytes\_swapped *= 4*[](#RsInstrument.BinFloatFormat.Double_8bytes_swapped "Link to this definition")

    Single\_4bytes *= 1*[](#RsInstrument.BinFloatFormat.Single_4bytes "Link to this definition")

    Single\_4bytes\_swapped *= 2*[](#RsInstrument.BinFloatFormat.Single_4bytes_swapped "Link to this definition")

*class* BinIntFormat(*value*)[[source]](_modules/RsInstrument/Internal/Conversions.html#BinIntFormat)[](#RsInstrument.BinIntFormat "Link to this definition")
:   Bases: `Enum`

    Binary format of an integer number.

    Integer16\_2bytes *= 3*[](#RsInstrument.BinIntFormat.Integer16_2bytes "Link to this definition")

    Integer16\_2bytes\_swapped *= 4*[](#RsInstrument.BinIntFormat.Integer16_2bytes_swapped "Link to this definition")

    Integer32\_4bytes *= 1*[](#RsInstrument.BinIntFormat.Integer32_4bytes "Link to this definition")

    Integer32\_4bytes\_swapped *= 2*[](#RsInstrument.BinIntFormat.Integer32_4bytes_swapped "Link to this definition")

*exception* DriverValueError(*rsrc\_name: str*, *message: str*)[[source]](_modules/RsInstrument/Internal/InstrumentErrors.html#DriverValueError)[](#RsInstrument.DriverValueError "Link to this definition")
:   Bases: [`RsInstrException`](#RsInstrument.RsInstrException "RsInstrument.Internal.InstrumentErrors.RsInstrException")

    Exception for different driver value settings e.g. RepCap values or Enum values.

*class* IoTransferEventArgs(*reading: bool*, *opc\_sync: bool*, *total\_size: int | None*, *context: str*)[[source]](_modules/RsInstrument/Internal/IoTransferEventArgs.html#IoTransferEventArgs)[](#RsInstrument.IoTransferEventArgs "Link to this definition")
:   Bases: `object`

    Contains event data for driver read or write operations.

    Initializes new instance of IoTransferEventArgs
    :param reading: True: reading operation, False: writing operation
    :param opc\_sync: defines if the command is OPC-synchronised
    :param total\_size: total size of the data received
    :param context: SCPI query. It is truncated to maximum of 100 characters

    binary*: bool*[](#RsInstrument.IoTransferEventArgs.binary "Link to this definition")
    :   string data

        Type:
        :   True

        Type:
        :   Binary data, False

    chunk\_ix*: int*[](#RsInstrument.IoTransferEventArgs.chunk_ix "Link to this definition")
    :   0-based index of the chunk.

    chunk\_size*: int*[](#RsInstrument.IoTransferEventArgs.chunk_size "Link to this definition")
    :   Size of one chunk of data. This number does not change during the transfer.

    data*: str | bytes*[](#RsInstrument.IoTransferEventArgs.data "Link to this definition")
    :   If the feature of transferring data over R/W event is switched ON, this field contains the whole data.

    id\_generator *= count(100)*[](#RsInstrument.IoTransferEventArgs.id_generator "Link to this definition")

    *classmethod* read\_chunk(*opc\_sync: bool*, *context: str*) → [IoTransferEventArgs](#RsInstrument.IoTransferEventArgs "RsInstrument.Internal.IoTransferEventArgs.IoTransferEventArgs")[[source]](_modules/RsInstrument/Internal/IoTransferEventArgs.html#IoTransferEventArgs.read_chunk)[](#RsInstrument.IoTransferEventArgs.read_chunk "Link to this definition")
    :   Creates new IoTransferEventArgs of read string

        Parameters:
        :   * **opc\_sync** – defines if the command is OPC-synchronised
            * **context** – SCPI query. It is truncated to maximum of 100 characters.

        Returns:
        :   IoTransferEventArgs object of a read string operation.

    resource\_name*: str*[](#RsInstrument.IoTransferEventArgs.resource_name "Link to this definition")
    :   Visa Resource Name of the instrument that generated the data.

    set\_end\_of\_transfer()[[source]](_modules/RsInstrument/Internal/IoTransferEventArgs.html#IoTransferEventArgs.set_end_of_transfer)[](#RsInstrument.IoTransferEventArgs.set_end_of_transfer "Link to this definition")
    :   Sets fields to signal end of transfer.

    total\_chunks*: int*[](#RsInstrument.IoTransferEventArgs.total_chunks "Link to this definition")
    :   Expected number of chunks.

    *property* transfer\_id*: int*[](#RsInstrument.IoTransferEventArgs.transfer_id "Link to this definition")
    :   Unique number for each transfer for this Instrument.
        If the transfer is performed in more chunks, the transfer\_id stays the same during the whole transfer.

    *classmethod* write\_bin(*context: str*) → [IoTransferEventArgs](#RsInstrument.IoTransferEventArgs "RsInstrument.Internal.IoTransferEventArgs.IoTransferEventArgs")[[source]](_modules/RsInstrument/Internal/IoTransferEventArgs.html#IoTransferEventArgs.write_bin)[](#RsInstrument.IoTransferEventArgs.write_bin "Link to this definition")
    :   Creates new IoTransferEventArgs of read binary data

        Parameters:
        :   **context** – SCPI command. It is truncated to maximum of 100 characters.

        Returns:
        :   IoTransferEventArgs object of a write-binary-data operation.

    *classmethod* write\_str(*opc\_sync: bool*, *total\_size: int*, *context: str*) → [IoTransferEventArgs](#RsInstrument.IoTransferEventArgs "RsInstrument.Internal.IoTransferEventArgs.IoTransferEventArgs")[[source]](_modules/RsInstrument/Internal/IoTransferEventArgs.html#IoTransferEventArgs.write_str)[](#RsInstrument.IoTransferEventArgs.write_str "Link to this definition")
    :   Creates new IoTransferEventArgs of write string

        Parameters:
        :   * **opc\_sync** – defines if the command is OPC-synchronised
            * **total\_size** – size of the data to write
            * **context** – SCPI command write. It is truncated to maximum of 100 characters

        Returns:
        :   IoTransferEventArgs object of a write-string operation.

*class* LoggingMode(*value*)[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LoggingMode)[](#RsInstrument.LoggingMode "Link to this definition")
:   Bases: `Enum`

    Determines the format of the logging message.

    Default *= 3*[](#RsInstrument.LoggingMode.Default "Link to this definition")

    Errors *= 2*[](#RsInstrument.LoggingMode.Errors "Link to this definition")

    Off *= 0*[](#RsInstrument.LoggingMode.Off "Link to this definition")

    On *= 1*[](#RsInstrument.LoggingMode.On "Link to this definition")

*class* OpcSyncQueryMechanism(*value*)[[source]](_modules/RsInstrument/Internal/InstrumentSettings.html#OpcSyncQueryMechanism)[](#RsInstrument.OpcSyncQueryMechanism "Link to this definition")
:   Bases: `Enum`

    Mechanism to use when querying with OPC.

    also\_check\_mav *= 1*[](#RsInstrument.OpcSyncQueryMechanism.also_check_mav "Link to this definition")

    cls\_only\_check\_mav\_err\_queue *= 2*[](#RsInstrument.OpcSyncQueryMechanism.cls_only_check_mav_err_queue "Link to this definition")

    only\_check\_mav\_err\_queue *= 3*[](#RsInstrument.OpcSyncQueryMechanism.only_check_mav_err_queue "Link to this definition")

    standard *= 0*[](#RsInstrument.OpcSyncQueryMechanism.standard "Link to this definition")

*exception* ResourceError(*rsrc\_name: str*, *message: str*)[[source]](_modules/RsInstrument/Internal/InstrumentErrors.html#ResourceError)[](#RsInstrument.ResourceError "Link to this definition")
:   Bases: [`RsInstrException`](#RsInstrument.RsInstrException "RsInstrument.Internal.InstrumentErrors.RsInstrException")

    Exception for resource name - e.g. resource not found.

*exception* RsInstrException(*message: str*)[[source]](_modules/RsInstrument/Internal/InstrumentErrors.html#RsInstrException)[](#RsInstrument.RsInstrException "Link to this definition")
:   Bases: `Exception`

    Exception base class for all the RsInstrument exceptions.

*class* RsInstrument(*resource\_name: str*, *id\_query: bool = True*, *reset: bool = False*, *options: str = None*, *direct\_session: object = None*)[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument)[](#RsInstrument.RsInstrument "Link to this definition")
:   Bases: `object`

    Root class for remote-controlling instrument with SCPI commands.

    Initializes new RsInstrument session.

    Parameters:
    :   * **resource\_name** – VISA resource name, e.g. ‘TCPIP::192.168.2.1::INSTR’
        * **id\_query** – if True, the instrument’s model name is verified against the models supported by the driver and eventually throws an exception
        * **reset** – Resets the instrument (sends [\*](#id41)RST) command and clears its status syb-system
        * **direct\_session** – Another driver object or pyVisa object to reuse the session instead of opening a new session
        * **options** – string tokens alternating the driver settings. More tokens are separated by comma.

    Parameter options tokens examples:
    :   * `Simulate=True` - starts the session in simulation mode. Default: `False`
        * `SelectVisa=socketio` - uses no VISA implementation for socket connections - you do not need any VISA-C installation
        * `SelectVisa=rs` - forces usage of RohdeSchwarz Visa
        * `SelectVisa=ni` - forces usage of National Instruments Visa
        * `Profile = HM8123` - setting profile fitting the specific non-standard instruments. Available values: HM8123, CMQ, ATS, Minimal. Default: `none`
        * `OpenTimeout=5000` - sets timeout used at the session opening. This timeout is only used in waiting for a locked session to be freed. Default: `2000ms`
        * `ExclusiveLock=True` - opens the session with exclusive lock on the VISA level. Default: `False`
        * `QueryInstrumentStatus = False` - same as `driver.utilities.instrument_status_checking = False`. Default: `True`
        * `WriteDelay = 20, ReadDelay = 5` - introduces delay of 20ms before each write and 5ms before each read. Default: `0ms` for both
        * `TerminationCharacter = "\r"` - sets the termination character for reading. Default: `\n` (LineFeed or LF)
        * `AssureWriteWithTermChar = True` - makes sure each command/query is terminated with termination character. Default: Interface dependent
        * `AddTermCharToWriteBinBlock = True` - adds one additional LF to the end of the binary data (some instruments require that). Default: `False`
        * `DataChunkSize = 10E3` - maximum size of one write/read segment. If transferred data is bigger, it is split to more segments. Default: `1E7` bytes
        * `OpcTimeout = 10000` - same as driver.utilities.opc\_timeout = 10000. Default: `30000ms`
        * `VisaTimeout = 5000` - same as driver.utilities.visa\_timeout = 5000. Default: `10000ms`
        * `ViClearExeMode = Disabled` - viClear() execution mode. Default: `execute_on_all`
        * `OpcQueryAfterWrite = True` - same as driver.utilities.opc\_query\_after\_write = True. Default: `False`
        * `OpcWaitMode = OpcQuery` - mode for all the opc-synchronised write/reads. Other modes: StbPolling, StbPollingSlow, StbPollingSuperSlow. Default: `StbPolling`
        * `StbInErrorCheck = False` - if true, the driver checks errors with [\*](#id43)STB? If false, it uses SYST:ERR?. Default: `True`
        * `SkipStatusSystemSettings = False` - some instruments do not support full status system commands. In such case, set this value to True. Default: `False`
        * `SkipClearStatus = True` - set to True for instruments that do not support [\*](#id45)CLS command. Default: `False`
        * `DisableOpcQuery = True` - set to True for instruments that do not support [\*](#id47)OPC? query. Default: `False`
        * `EachCmdAsQuery = True`, set to True, for instruments that always return answer. Default: `false`
        * `CmdIdn = ID?` - defines which SCPI command to use for identification query. Use ‘<none>’ string to skip identification query at the init. Default: `*IDN?`
        * `CmdReset = RT` - defines which SCPI command to use for reset. Default: `*RST`
        * `VxiCapable = false` - you can force a session to a VXI-incapable. Default: <interface-dependent>
        * `Encoding = utf-8` - setting of encoding for strings into bytes and vice versa. Default: `charmap`
        * `OpcSyncQueryMechanism = AlsoCheckMav` - setting of mechanism for OPC-synchronised queries. Default: `OnlyCheckMavErrQueue`
        * `FirstCmds = *CLS` - first command(s) to sent after init. Separated more commands/queries with ‘;;’. Default: [``](#id49)[``](#id51)
        * `EachCmdPrefix = lf` - this prefix is added to the beginning of each command sent to the instrument. Default: [``](#id53)[``](#id55)
        * `EachCmdSuffix = cr` - this suffix is added to the end of each command sent to the instrument. Default: [``](#id57)[``](#id59)
        * `StripStringTrailingWhitespaces = True` - use it to strip white spaces from string query responses. Default: `False`
        * `LoggingMode = On` - sets the logging status right from the start. Possible values: On | Off | Error. Default: `Off`
        * `LoggingName = 'MyDevice'` - sets the name to represent the session in the log entries. Default: `<resource_name>`
        * `LoggingFormat = 'PAD_LEFT12(%START_TIME%) PAD_LEFT25(%DEVICE_NAME%) PAD_LEFT12(%DURATION%) %SCPI_COMMAND%'` - sets the format of the log entries. Default: `PAD_LEFT12(%START_TIME%) PAD_LEFT25(%DEVICE_NAME%) PAD_LEFT12(%DURATION%)  %LOG_STRING_INFO%: %LOG_STRING%`
        * `LogToGlobalTarget = True` - sets the logging target to the class-property previously set with RsInstrument.set\_global\_logging\_target() Default: `False`
        * `LoggingToConsole = True` - immediately starts logging to the console. Default: False
        * `LoggingToUdp = True` - immediately starts logging to the UDP port. Default: False
        * `LoggingUdpPort = 49200` - UDP port to log to. Default: 49200
        * `LoggingRelativeTimeOfFirstEntry = True` - Logging starts with relative time set to the first log entry, which causes the first start time to be ‘00:00:00.000’. Default: False

    add\_instr\_option(*option: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.add_instr_option)[](#RsInstrument.RsInstrument.add_instr_option "Link to this definition")
    :   Adds new option if not already existing.

    *static* assert\_minimum\_version(*min\_version: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.assert_minimum_version)[](#RsInstrument.RsInstrument.assert_minimum_version "Link to this definition")
    :   Asserts that the driver version fulfills the minimum required version you have entered.
        This way you make sure your installed driver is of the entered version or newer.

    assign\_lock(*lock: RLock*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.assign_lock)[](#RsInstrument.RsInstrument.assign_lock "Link to this definition")
    :   Assigns the provided thread lock.

    *property* bin\_float\_numbers\_format*: [BinFloatFormat](#RsInstrument.BinFloatFormat "RsInstrument.Internal.Conversions.BinFloatFormat")*[](#RsInstrument.RsInstrument.bin_float_numbers_format "Link to this definition")
    :   Sets / returns format of float numbers when transferred as binary data

    *property* bin\_int\_numbers\_format*: [BinIntFormat](#RsInstrument.BinIntFormat "RsInstrument.Internal.Conversions.BinIntFormat")*[](#RsInstrument.RsInstrument.bin_int_numbers_format "Link to this definition")
    :   Sets / returns format of integer numbers when transferred as binary data

    check\_status() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.check_status)[](#RsInstrument.RsInstrument.check_status "Link to this definition")
    :   Throws InstrumentStatusException in case of an error in the instrument’s error queue.
        The status checking is performed always, independent of the property ‘instrument\_status\_checking’.
        Also, the property ScpiLogger.log\_status\_check\_ok is ignored, and the Status check is always logged.

    *classmethod* clear\_global\_logging\_relative\_timestamp() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.clear_global_logging_relative_timestamp)[](#RsInstrument.RsInstrument.clear_global_logging_relative_timestamp "Link to this definition")
    :   Clears the global relative timestamp. After this, all the instances using the global relative timestamp continue logging with the absolute timestamps.

    clear\_lock() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.clear_lock)[](#RsInstrument.RsInstrument.clear_lock "Link to this definition")
    :   Clears the existing thread lock, making the current session thread-independent from others that might share the current thread lock.

    clear\_status() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.clear_status)[](#RsInstrument.RsInstrument.clear_status "Link to this definition")
    :   Clears instrument’s status system, the session’s I/O buffers and the instrument’s error queue

    close() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.close)[](#RsInstrument.RsInstrument.close "Link to this definition")
    :   Closes the active RsInstrument session

    *property* data\_chunk\_size*: int*[](#RsInstrument.RsInstrument.data_chunk_size "Link to this definition")
    :   Returns max chunk size of one data block.

    *property* driver\_version*: str*[](#RsInstrument.RsInstrument.driver_version "Link to this definition")
    :   Returns the RsInstrument package version

    *property* encoding*: str*[](#RsInstrument.RsInstrument.encoding "Link to this definition")
    :   Returns string<=>bytes encoding of the session.

    *property* events*: [Events](events.html#RsInstrument.Fixed_Files.Events.Events "RsInstrument.Fixed_Files.Events.Events")*[](#RsInstrument.RsInstrument.events "Link to this definition")
    :   Interface for event handlers, see [here](events.html#events)

    file\_exists(*instr\_file: str*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.file_exists)[](#RsInstrument.RsInstrument.file_exists "Link to this definition")
    :   Returns true, if the instrument file exist.

    *classmethod* from\_existing\_session(*session: object*, *options: str = None*) → [RsInstrument](#RsInstrument.RsInstrument.RsInstrument "RsInstrument.RsInstrument.RsInstrument")[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.from_existing_session)[](#RsInstrument.RsInstrument.from_existing_session "Link to this definition")
    :   Creates a new RsInstrument object with the entered ‘session’ reused.
        :param session: can be another driver or a direct pyvisa session.
        :param options: string tokens alternating the driver settings. More tokens are separated by comma.

    *property* full\_instrument\_model\_name*: str*[](#RsInstrument.RsInstrument.full_instrument_model_name "Link to this definition")
    :   Returns the current instrument’s full name e.g. ‘FSW26’

    *classmethod* get\_driver\_version() → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_driver_version)[](#RsInstrument.RsInstrument.get_driver_version "Link to this definition")
    :   Returns the RsInstrument package version

    get\_file\_size(*instr\_file: str*) → int | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_file_size)[](#RsInstrument.RsInstrument.get_file_size "Link to this definition")
    :   Return size of the instrument file, or None if the file does not exist.

    *classmethod* get\_global\_logging\_relative\_timestamp() → datetime | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_global_logging_relative_timestamp)[](#RsInstrument.RsInstrument.get_global_logging_relative_timestamp "Link to this definition")
    :   Returns global common relative timestamp for log entries.

    *classmethod* get\_global\_logging\_target()[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_global_logging_target)[](#RsInstrument.RsInstrument.get_global_logging_target "Link to this definition")
    :   Returns global common target stream.

    get\_last\_sent\_cmd() → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_last_sent_cmd)[](#RsInstrument.RsInstrument.get_last_sent_cmd "Link to this definition")
    :   Returns the last commands sent to the instrument. Only works in simulation mode.

    get\_lock() → RLock[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_lock)[](#RsInstrument.RsInstrument.get_lock "Link to this definition")
    :   Returns the thread lock for the current session.

        By default:

        * If you create a new RsInstrument instance with new VISA session, the session gets a new thread lock. You can assign it to another RsInstrument sessions in order to share one physical instrument with a multi-thread access.
        * If you create a new RsInstrument from an existing session, the thread lock is shared automatically making both instances multi-thread safe.

        You can always assign new thread lock by calling `driver.utilities.assign_lock()`

    get\_session\_handle()[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_session_handle)[](#RsInstrument.RsInstrument.get_session_handle "Link to this definition")
    :   Returns the underlying pyvisa session

    get\_total\_execution\_time() → timedelta[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_total_execution_time)[](#RsInstrument.RsInstrument.get_total_execution_time "Link to this definition")
    :   Returns total time spent by the library on communicating with the instrument.
        This time is always shorter than get\_total\_time(), since it does not include gaps between the communication.
        You can reset this counter with reset\_time\_statistics().

    get\_total\_time() → timedelta[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_total_time)[](#RsInstrument.RsInstrument.get_total_time "Link to this definition")
    :   Returns delta time spent by the library between the get\_total\_time\_startpoint() and now.
        This time is always longer than get\_total\_execution\_time(), since it also includes all other activities besides the communication.
        You can set the total time startpoint to now with reset\_time\_statistics().

    get\_total\_time\_startpoint() → datetime[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.get_total_time_startpoint)[](#RsInstrument.RsInstrument.get_total_time_startpoint "Link to this definition")
    :   Returns time from which the execution started.
        This is the value that the get\_total\_time() calculates as its reference.
        Calling the reset\_time\_statistics() sets this time to now.

    go\_to\_local(*mixed\_mode: bool = True*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.go_to_local)[](#RsInstrument.RsInstrument.go_to_local "Link to this definition")
    :   Puts the instrument into local state.
        By default, the method uses a mechanism to keep the instrument in a mixed mode: remote and local.
        That means, you can remote-control your instrument, and at the same time it still allows manual control.
        Set the mixed\_mode to False, if you want your instrument to go to remote mode as soon as it receives the first remote command.

    go\_to\_remote() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.go_to_remote)[](#RsInstrument.RsInstrument.go_to_remote "Link to this definition")
    :   Puts the instrument into remote state.

    has\_instr\_option(*options: str | List[str]*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.has_instr_option)[](#RsInstrument.RsInstrument.has_instr_option "Link to this definition")
    :   Returns true, if the entered options (case-insensitive) matches at least one of the installed options (or-logic).
        You can enter either a string with one option, or more options ‘/’-separated, or more options as a list of strings.
        If K0 is present, all the K-options are reported as present. B-options are not affected by K0.
        Example 1: options=’k23’ returns true, if the instrument has the option ‘K23’.
        Example 2: options=’k23 / K23e’ returns true, if the instrument has either the option ‘K23’ or the option ‘K23E’.
        Example 3: options=[‘k11’,’K22’] returns true, if the instrument has either the option ‘K11’ or the option ‘K22’.

    has\_instr\_option\_k0() → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.has_instr_option_k0)[](#RsInstrument.RsInstrument.has_instr_option_k0 "Link to this definition")
    :   Returns true, if the instrument has K0 installed.

    has\_instr\_option\_regex(*re\_options: str | List[str]*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.has_instr_option_regex)[](#RsInstrument.RsInstrument.has_instr_option_regex "Link to this definition")
    :   Returns true, if the entered regex string (case-insensitive) matches at least one of the installed options.
        The match must be complete, not just partial (search).
        You can enter either a string with one option, or more options ‘/’-separated, or more options as a list of strings.
        Example 1: re\_options=’k10.’ returns true, if the instrument contains any option ‘K100’ … up to ‘K109’ .
        Example 2: re\_options=’k10. / k20.\*’ returns true, if the instrument contains any of the options ‘K10x’ or ‘K20xxx’.
        Example 3: re\_options=[‘k10.’, ‘k20.\*’] returns true, if the instrument contains any options ‘K10x’ or ‘K20xxx’.

    *property* idn\_string*: str*[](#RsInstrument.RsInstrument.idn_string "Link to this definition")
    :   Returns instrument’s identification string - the response on the SCPI command [\*](#id61)IDN?

    instr\_err\_suppressor(*visa\_tout\_ms: int = 0*, *suppress\_only\_codes: int | List[int] = None*) → InstrErrorSuppressor[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.instr_err_suppressor)[](#RsInstrument.RsInstrument.instr_err_suppressor "Link to this definition")
    :   Returns Context Manager that suppresses the instrument errors.
        Other exceptions types are still raised.
        On entering the context, this class clears all the instrument status errors.
        :param visa\_tout\_ms: VISA Timeout in milliseconds, that is set for this context. Afterward, it is changed back. Default value: do-not-change.
        :param suppress\_only\_codes: You can enter a code or list of codes for errors to be suppressed. Other errors will be reported. Example: If you enter -113 here, only the ‘Undefined Header’ error will be suppressed. Default value: suppress-all-errors.

    *property* instrument\_firmware\_version*: str*[](#RsInstrument.RsInstrument.instrument_firmware_version "Link to this definition")
    :   Returns instrument’s firmware version

    *property* instrument\_model\_name*: str*[](#RsInstrument.RsInstrument.instrument_model_name "Link to this definition")
    :   Returns the current instrument’s family name e.g. ‘FSW’

    *property* instrument\_options*: List[str]*[](#RsInstrument.RsInstrument.instrument_options "Link to this definition")
    :   Returns all the instrument options.
        The options are sorted in the ascending order starting with K-options and continuing with B-options

    *property* instrument\_serial\_number*: str*[](#RsInstrument.RsInstrument.instrument_serial_number "Link to this definition")
    :   Returns instrument’s serial\_number

    *property* instrument\_status\_checking*: bool*[](#RsInstrument.RsInstrument.instrument_status_checking "Link to this definition")
    :   Sets / returns Instrument Status Checking.
        When True (default is True), all the driver methods and properties are sending “SYSTem:ERRor?”
        at the end to immediately react on error that might have occurred.
        We recommend keeping the state checking ON all the time. Switch it OFF only in rare cases when you require maximum speed.
        The default state after initializing the session is ON.

    is\_connection\_active() → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.is_connection_active)[](#RsInstrument.RsInstrument.is_connection_active "Link to this definition")
    :   Returns true, if the VISA connection is active and the communication with the instrument still works.
        WARNING!!! this method queries the session’s VISA Timeout and additionally, queries the [\*](#id63)IDN? from the instrument,
        hence affects the performance of your application when used regularly.

    *static* list\_resources(*expression: str = '?\*::INSTR'*, *visa\_select: str = None*) → List[str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.list_resources)[](#RsInstrument.RsInstrument.list_resources "Link to this definition")
    :   Finds all the resources defined by the expression.

        * ‘?\*’ - matches all the available instruments
        * ‘USB::?\*’ - matches all the USB instruments
        * ‘TCPIP::192?\*’ - matches all the LAN instruments with the IP address starting with 192

        Parameters:
        :   * **expression** – see the examples in the function
            * **visa\_select** – optional parameter selecting a specific VISA. Examples: [‘@ivi](mailto:'%40ivi)’, [‘@rs](mailto:'%40rs)’

    lock\_resource(*timeout: int*, *requested\_key: str | bytes = None*) → bytes | str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.lock_resource)[](#RsInstrument.RsInstrument.lock_resource "Link to this definition")
    :   Locks the instrument to prevent it from communicating with other clients.

    *property* logger*: [ScpiLogger](logger.html#RsInstrument.Internal.ScpiLogger.ScpiLogger "RsInstrument.Internal.ScpiLogger.ScpiLogger")*[](#RsInstrument.RsInstrument.logger "Link to this definition")
    :   Scpi Logger interface, see [here](logger.html#logger)

    *property* manufacturer*: str*[](#RsInstrument.RsInstrument.manufacturer "Link to this definition")
    :   Returns manufacturer of the instrument

    *property* opc\_query\_after\_write*: bool*[](#RsInstrument.RsInstrument.opc_query_after_write "Link to this definition")
    :   Sets / returns Instrument [\*](#id65)OPC? query sending after each command write.
        When True, (default is False) the driver sends [\*](#id67)OPC? every time a write command is performed.
        Use this if you want to make sure your sequence is performed command-after-command.

    *property* opc\_sync\_query\_mechanism*: [OpcSyncQueryMechanism](#RsInstrument.OpcSyncQueryMechanism "RsInstrument.Internal.InstrumentSettings.OpcSyncQueryMechanism")*[](#RsInstrument.RsInstrument.opc_sync_query_mechanism "Link to this definition")
    :   Returns the current setting of the OPC-Sync query mechanism.

    *property* opc\_timeout*: int*[](#RsInstrument.RsInstrument.opc_timeout "Link to this definition")
    :   Sets / returns timeout in milliseconds for all the operations that use OPC synchronization.

    process\_all\_commands() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.process_all_commands)[](#RsInstrument.RsInstrument.process_all_commands "Link to this definition")
    :   SCPI command: [\*](#id69)WAI
        Stops further commands processing until all commands sent before [\*](#id71)WAI have been executed.

    query(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query)[](#RsInstrument.RsInstrument.query "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        This method is an alias to the query\_str() method.

    query\_all\_errors() → List[str] | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_all_errors)[](#RsInstrument.RsInstrument.query_all_errors "Link to this definition")
    :   Queries and clears all the errors from the instrument’s error queue.
        The method returns list of strings as error messages. If no error is detected, the return value is None.
        The process is: querying ‘SYSTem:ERRor?’ in a loop until the error queue is empty.
        If you want to include the error codes, call the query\_all\_errors\_with\_codes()

    query\_all\_errors\_with\_codes() → List[Tuple[int, str]] | None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_all_errors_with_codes)[](#RsInstrument.RsInstrument.query_all_errors_with_codes "Link to this definition")
    :   Queries and clears all the errors from the instrument’s error queue.
        The method returns list of tuples (code: int, message: str). If no error is detected, the return value is None.
        The process is: querying ‘SYSTem:ERRor?’ in a loop until the error queue is empty.

    query\_bin\_block(*query: str*) → bytes[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block)[](#RsInstrument.RsInstrument.query_bin_block "Link to this definition")
    :   Queries binary data block to bytes.
        Throws an exception if the returned data was not a binary data.
        Returns <data:bytes>

    query\_bin\_block\_to\_file(*query: str*, *file\_path: str*, *append: bool = False*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block_to_file)[](#RsInstrument.RsInstrument.query_bin_block_to_file "Link to this definition")
    :   Queries binary data block to the provided file.
        If append is False, any existing file content is discarded.
        If append is True, the new content is added to the end of the existing file, or if the file does not exit, it is created.
        Throws an exception if the returned data was not a binary data.
        Example for transferring a file from Instrument -> PC:
        query = f”MMEM:DATA? ‘{INSTR\_FILE\_PATH}’”.

        Alternatively, use the dedicated methods for this purpose:

        * `send_file_from_pc_to_instrument()`
        * `read_file_from_instrument_to_pc()`

    query\_bin\_block\_to\_file\_with\_opc(*query: str*, *file\_path: str*, *append: bool = False*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block_to_file_with_opc)[](#RsInstrument.RsInstrument.query_bin_block_to_file_with_opc "Link to this definition")
    :   Sends a OPC-synced query and writes the returned data to the provided file.
        If append is False, any existing file content is discarded.
        If append is True, the new content is added to the end of the existing file, or if the file does not exit, it is created.
        Throws an exception if the returned data was not a binary data.

    query\_bin\_block\_with\_opc(*query: str*, *timeout: int = None*) → bytes[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_block_with_opc)[](#RsInstrument.RsInstrument.query_bin_block_with_opc "Link to this definition")
    :   Sends a OPC-synced query and returns binary data block to bytes.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_bin\_or\_ascii\_float\_list(*query: str*) → List[float][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_float_list)[](#RsInstrument.RsInstrument.query_bin_or_ascii_float_list "Link to this definition")
    :   Queries a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

    query\_bin\_or\_ascii\_float\_list\_with\_opc(*query: str*, *timeout: int = None*) → List[float][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_float_list_with_opc)[](#RsInstrument.RsInstrument.query_bin_or_ascii_float_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

        If you do not provide timeout, the method uses current opc\_timeout.

    query\_bin\_or\_ascii\_int\_list(*query: str*) → List[int][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_int_list)[](#RsInstrument.RsInstrument.query_bin_or_ascii_int_list "Link to this definition")
    :   Queries a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

    query\_bin\_or\_ascii\_int\_list\_with\_opc(*query: str*, *timeout: int = None*) → List[int][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bin_or_ascii_int_list_with_opc)[](#RsInstrument.RsInstrument.query_bin_or_ascii_int_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads a list of floating-point numbers that can be returned as ASCII or binary format.

        * For ASCII format, the list numbers are decoded as comma-separated values.
        * For Binary Format, the numbers are decoded based on the property BinFloatFormat, usually float 32-bit (FORM REAL,32).

        If you do not provide timeout, the method uses current opc\_timeout.

    query\_bool(*query: str*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool)[](#RsInstrument.RsInstrument.query_bool "Link to this definition")
    :   Sends the query to the instrument and returns the response as boolean.

    query\_bool\_list(*query: str*) → List[bool][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool_list)[](#RsInstrument.RsInstrument.query_bool_list "Link to this definition")
    :   Sends the string query to the instrument and returns the response as List of booleans,
        where the delimiter is comma (‘,’).
        Blank or empty response is returned as an empty list.

    query\_bool\_list\_with\_opc(*query: str*, *timeout: int = None*) → List[bool][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool_list_with_opc)[](#RsInstrument.RsInstrument.query_bool_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads response from the instrument as csv-list of booleans.
        If you do not provide timeout, the method uses current opc\_timeout.
        Blank or empty response is returned as an empty list.

    query\_bool\_with\_opc(*query: str*, *timeout: int = None*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_bool_with_opc)[](#RsInstrument.RsInstrument.query_bool_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as boolean.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_float(*query: str*) → float[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_float)[](#RsInstrument.RsInstrument.query_float "Link to this definition")
    :   Sends the query to the instrument and returns the response as float.

    query\_float\_with\_opc(*query: str*, *timeout: int = None*) → float[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_float_with_opc)[](#RsInstrument.RsInstrument.query_float_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as float.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_int(*query: str*) → int[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_int)[](#RsInstrument.RsInstrument.query_int "Link to this definition")
    :   Sends the query to the instrument and returns the response as integer.

    query\_int\_with\_opc(*query: str*, *timeout: int = None*) → int[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_int_with_opc)[](#RsInstrument.RsInstrument.query_int_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as integer.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_opc(*timeout: int = 0*) → int[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_opc)[](#RsInstrument.RsInstrument.query_opc "Link to this definition")
    :   SCPI command: [\*](#id73)OPC?
        Queries the instrument’s OPC bit and hence it waits until the instrument reports operation complete.
        If you define timeout > 0, the VISA timeout is set to that value just for this method call.

    query\_str(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str)[](#RsInstrument.RsInstrument.query_str "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        This method is an alias to the query() method.

    query\_str\_list(*query: str*, *remove\_blank\_response: bool = False*) → List[str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_list)[](#RsInstrument.RsInstrument.query_str_list "Link to this definition")
    :   Sends the string query to the instrument and returns the response as List of strings, where the delimiter is comma (‘,’). Each element of the list is trimmed for leading and trailing quotes.

        Meaning of the ‘remove\_blank\_response’:
        :   * False(default): whitespaces-only response is returned as a list with one empty element [‘’].
            * True: whitespaces-only response is returned as an empty list [].

    query\_str\_list\_with\_opc(*query: str*, *timeout: int = None*, *remove\_blank\_response: bool = False*) → List[str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_list_with_opc)[](#RsInstrument.RsInstrument.query_str_list_with_opc "Link to this definition")
    :   Sends a OPC-synced query and reads response from the instrument as csv-list.
        :   If you do not provide timeout, the method uses current opc\_timeout.

        Meaning of the ‘remove\_blank\_response’:
        :   * False(default): whitespaces-only response is returned as a list with one empty element [‘’].
            * True: whitespaces-only response is returned as an empty list [].

    query\_str\_stripped(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_stripped)[](#RsInstrument.RsInstrument.query_str_stripped "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string stripped of the trailing LF and leading/trailing single/double quotes.
        The stripping of the leading/trailing quotes is blocked, if the string contains the quotes in the middle.
        This method is an alias to the query\_stripped() method.

    query\_str\_with\_opc(*query: str*, *timeout: int = None*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_str_with_opc)[](#RsInstrument.RsInstrument.query_str_with_opc "Link to this definition")
    :   Sends the opc-synced query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        If you do not provide timeout, the method uses current opc\_timeout.

    query\_stripped(*query: str*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_stripped)[](#RsInstrument.RsInstrument.query_stripped "Link to this definition")
    :   Sends the string query to the instrument and returns the response as string stripped of the trailing LF and leading/trailing single/double quotes.
        The stripping of the leading/trailing quotes is blocked, if the string contains the quotes in the middle.

    query\_with\_opc(*query: str*, *timeout: int = None*) → str[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.query_with_opc)[](#RsInstrument.RsInstrument.query_with_opc "Link to this definition")
    :   This method is an alias to the write\_str\_with\_opc().
        Sends the opc-synced query to the instrument and returns the response as string.
        The response is trimmed of any trailing LF characters and has no length limit.
        If you do not provide timeout, the method uses current opc\_timeout.

    read\_file\_from\_instrument\_to\_pc(*source\_instr\_file: str*, *target\_pc\_file: str*, *append\_to\_pc\_file: bool = False*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.read_file_from_instrument_to_pc)[](#RsInstrument.RsInstrument.read_file_from_instrument_to_pc "Link to this definition")
    :   SCPI Command: MMEM:DATA?

        Reads file from instrument to the PC.

        Set the `append_to_pc_file` to True if you want to append the read content to the end of the existing PC file.

    reconnect(*force\_close: bool = False*) → bool[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.reconnect)[](#RsInstrument.RsInstrument.reconnect "Link to this definition")
    :   If the connection is not active, the method tries to reconnect to the device.
        If the connection is active, and force\_close is False, the method does nothing.
        If the connection is active, and force\_close is True, the method closes, and opens the session again.
        Returns True, if the reconnection has been performed.

    remove\_instr\_option(*option: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.remove_instr_option)[](#RsInstrument.RsInstrument.remove_instr_option "Link to this definition")
    :   Removes the option if exists.

    reset(*timeout: int = 0*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.reset)[](#RsInstrument.RsInstrument.reset "Link to this definition")
    :   SCPI command: [\*](#id75)RST
        Sends [\*](#id77)RST command + calls the clear\_status().
        If you define timeout > 0, the VISA timeout is set to that value just for this method call.

    reset\_time\_statistics() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.reset_time_statistics)[](#RsInstrument.RsInstrument.reset_time_statistics "Link to this definition")
    :   Resets all execution and total time counters.
        Affects the results of get\_total\_time(), get\_total\_execution\_time() and get\_total\_time\_startpoint()

    *property* resource\_name*: str*[](#RsInstrument.RsInstrument.resource_name "Link to this definition")
    :   Returns the resource name used in the constructor.

    self\_test(*timeout: int = None*) → Tuple[int, str][[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.self_test)[](#RsInstrument.RsInstrument.self_test "Link to this definition")
    :   SCPI command: [\*](#id79)TST?
        Performs instrument’s self-test.
        Returns tuple (code:int, message: str). Code 0 means the self-test passed.
        You can define the custom timeout in milliseconds. If you do not define it, the method uses default self-test timeout (usually 60 secs).

    send\_file\_from\_pc\_to\_instrument(*source\_pc\_file: str*, *target\_instr\_file: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.send_file_from_pc_to_instrument)[](#RsInstrument.RsInstrument.send_file_from_pc_to_instrument "Link to this definition")
    :   SCPI Command: MMEM:DATA

        Sends file from PC to the instrument.

    *classmethod* set\_global\_logging\_relative\_time\_of\_first\_entry() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_relative_time_of_first_entry)[](#RsInstrument.RsInstrument.set_global_logging_relative_time_of_first_entry "Link to this definition")
    :   This method sets the global flag, that takes the very first log entry start time of any global instance as a global relative timestamp.
        This means, after this call, the first instance that logs an entry set the relative timestamp for all global target instances,
        and begins with the start timestamp 0:00:00.000

    *classmethod* set\_global\_logging\_relative\_timestamp(*timestamp: datetime*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_relative_timestamp)[](#RsInstrument.RsInstrument.set_global_logging_relative_timestamp "Link to this definition")
    :   Sets global common relative timestamp for log entries. To use it, call the following: io.logger.set\_relative\_timestamp\_global()

    *classmethod* set\_global\_logging\_relative\_timestamp\_now() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_relative_timestamp_now)[](#RsInstrument.RsInstrument.set_global_logging_relative_timestamp_now "Link to this definition")
    :   Sets global common relative timestamp for log entries to this moment.
        To use it, call the following: io.logger.set\_relative\_timestamp\_global().

    *classmethod* set\_global\_logging\_target(*target*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.set_global_logging_target)[](#RsInstrument.RsInstrument.set_global_logging_target "Link to this definition")
    :   Sets global common target stream that each instance can use. To use it, call the following: io.logger.set\_logging\_target\_global().
        If an instance uses global logging target, it automatically uses the global relative timestamp (if set).
        You can set the target to None to invalidate it.

    *property* supported\_models*: List[str]*[](#RsInstrument.RsInstrument.supported_models "Link to this definition")
    :   Returns a list of the instrument models supported by this instrument driver

    unlock\_resource() → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.unlock_resource)[](#RsInstrument.RsInstrument.unlock_resource "Link to this definition")
    :   Unlocks the instrument to other clients.

    *property* visa\_manufacturer*: str*[](#RsInstrument.RsInstrument.visa_manufacturer "Link to this definition")
    :   Returns the manufacturer of the current VISA session.

    *property* visa\_timeout*: int*[](#RsInstrument.RsInstrument.visa_timeout "Link to this definition")
    :   Sets / returns visa IO timeout in milliseconds.

    visa\_tout\_suppressor(*visa\_tout\_ms: int = 0*) → VisaTimeoutSuppressor[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.visa_tout_suppressor)[](#RsInstrument.RsInstrument.visa_tout_suppressor "Link to this definition")
    :   Returns Context Manager that suppresses the VISA timeout error.
        Careful!!!: Only the very first VISA Timeout exception is suppressed,
        and afterward the context ends. Therefore, use only one command per context manager,
        if you do not want to skip the following ones.
        :param visa\_tout\_ms: VISA Timeout in milliseconds, that is set for this context. Afterward, it is changed back. Default value: do-not-change.

    write(*cmd: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write)[](#RsInstrument.RsInstrument.write "Link to this definition")
    :   Writes the command to the instrument as string.
        This method is an alias to the write\_str() method.

    write\_bin\_block(*cmd: str*, *payload: bytes*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bin_block)[](#RsInstrument.RsInstrument.write_bin_block "Link to this definition")
    :   Writes all the payload as binary data block to the instrument.
        The binary data header is added at the beginning of the transmission automatically, do not include it in the payload!!!

    write\_bin\_block\_from\_file(*cmd: str*, *file\_path: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bin_block_from_file)[](#RsInstrument.RsInstrument.write_bin_block_from_file "Link to this definition")
    :   Writes data from the file as binary data block to the instrument using the provided command.
        Example for transferring a file from PC -> Instrument:
        cmd = f”MMEM:DATA ‘{INSTR\_FILE\_PATH}’,”.

        Alternatively, use the dedicated methods for this purpose:

        * `send_file_from_pc_to_instrument()`
        * `read_file_from_instrument_to_pc()`

    write\_bool(*cmd: str*, *param: bool*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bool)[](#RsInstrument.RsInstrument.write_bool "Link to this definition")
    :   Writes the command to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘OUTPUT’ param = ‘True’, result command = ‘OUTPUT ON’

    write\_bool\_with\_opc(*cmd: str*, *param: bool*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_bool_with_opc)[](#RsInstrument.RsInstrument.write_bool_with_opc "Link to this definition")
    :   Writes the command with OPC to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘OUTPUT’ param = ‘True’, result command = ‘OUTPUT ON’
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_float(*cmd: str*, *param: float*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_float)[](#RsInstrument.RsInstrument.write_float "Link to this definition")
    :   Writes the command to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘CENTER:FREQ’ param = ‘10E6’, result command = ‘CENTER:FREQ 10E6’

    write\_float\_with\_opc(*cmd: str*, *param: float*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_float_with_opc)[](#RsInstrument.RsInstrument.write_float_with_opc "Link to this definition")
    :   Writes the command with OPC to the instrument followed by the boolean parameter:
        e.g.: cmd = ‘CENTER:FREQ’ param = ‘10E6’, result command = ‘CENTER:FREQ 10E6’
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_int(*cmd: str*, *param: int*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_int)[](#RsInstrument.RsInstrument.write_int "Link to this definition")
    :   Writes the command to the instrument followed by the integer parameter:
        e.g.: cmd = ‘SELECT:INPUT’ param = ‘2’, result command = ‘SELECT:INPUT 2’

    write\_int\_with\_opc(*cmd: str*, *param: int*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_int_with_opc)[](#RsInstrument.RsInstrument.write_int_with_opc "Link to this definition")
    :   Writes the command with OPC to the instrument followed by the integer parameter:
        e.g.: cmd = ‘SELECT:INPUT’ param = ‘2’, result command = ‘SELECT:INPUT 2’
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_str(*cmd: str*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_str)[](#RsInstrument.RsInstrument.write_str "Link to this definition")
    :   Writes the command to the instrument as string.
        This method is an alias to write() method.

    write\_str\_with\_opc(*cmd: str*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_str_with_opc)[](#RsInstrument.RsInstrument.write_str_with_opc "Link to this definition")
    :   Writes the opc-synced command to the instrument.
        If you do not provide timeout, the method uses current opc\_timeout.

    write\_with\_opc(*cmd: str*, *timeout: int = None*) → None[[source]](_modules/RsInstrument/RsInstrument.html#RsInstrument.write_with_opc)[](#RsInstrument.RsInstrument.write_with_opc "Link to this definition")
    :   This method is an alias to the write\_str\_with\_opc().
        Writes the opc-synced command to the instrument.
        If you do not provide timeout, the method uses current opc\_timeout.

*exception* StatusException(*rsrc\_name: str*, *message: str*, *errors\_list: List[Tuple[int, str]]*, *first\_exc: type = None*)[[source]](_modules/RsInstrument/Internal/InstrumentErrors.html#StatusException)[](#RsInstrument.StatusException "Link to this definition")
:   Bases: [`RsInstrException`](#RsInstrument.RsInstrException "RsInstrument.Internal.InstrumentErrors.RsInstrException")

    Exception for instrument status errors.
    Tje field errors\_list contains the complete list of all the errors with messages and codes.

*exception* TimeoutException(*message: str*)[[source]](_modules/RsInstrument/Internal/InstrumentErrors.html#TimeoutException)[](#RsInstrument.TimeoutException "Link to this definition")
:   Bases: [`RsInstrException`](#RsInstrument.RsInstrException "RsInstrument.Internal.InstrumentErrors.RsInstrException")

    Exception for timeout errors.

*exception* UnexpectedResponseException(*rsrc\_name: str*, *message: str*)[[source]](_modules/RsInstrument/Internal/InstrumentErrors.html#UnexpectedResponseException)[](#RsInstrument.UnexpectedResponseException "Link to this definition")
:   Bases: [`RsInstrException`](#RsInstrument.RsInstrException "RsInstrument.Internal.InstrumentErrors.RsInstrException")

    Exception for instrument unexpected responses.

size\_to\_kb\_mb\_gb\_string(*data\_size: int*, *as\_additional\_info: bool = False*, *allow\_gb: bool = True*) → str[[source]](_modules/RsInstrument/Internal/Utilities.html#size_to_kb_mb_gb_string)[](#RsInstrument.size_to_kb_mb_gb_string "Link to this definition")
:   Returns human-readable string with kilobytes, megabytes or gigabytes
    depending on the data\_size range.

    > param data\_size:
    > :   data size in bytes to convert
    >
    > param allow\_gb:
    > :   allow also Gigabytes size
    >
    > param as\_additional\_info:
    >
    > if True, the dynamic data appear in round bracket after the number in bytes. e.g. ‘12345678 bytes (11.7 MB)’
    > if False, only the dynamic data is returned e.g. ‘11.7 MB’

size\_to\_kb\_mb\_string(*data\_size: int*, *as\_additional\_info: bool = False*) → str[[source]](_modules/RsInstrument/Internal/Utilities.html#size_to_kb_mb_string)[](#RsInstrument.size_to_kb_mb_string "Link to this definition")
:   Returns human-readable string with kilobytes or megabytes depending on the data\_size range.

    Parameters:
    :   * **data\_size** – data size in bytes to convert
        * **as\_additional\_info**

    if True, the dynamic data appear in round bracket after the number in bytes. e.g. ‘12345678 bytes (11.7 MB)’
    if False, only the dynamic data is returned e.g. ‘11.7 MB’

value\_to\_si\_string(*value: float*, *fmt: str = '.12g'*, *min\_decimal\_places: int = 0*, *str\_after\_number: str = ' '*) → str[[source]](_modules/RsInstrument/Internal/Utilities.html#value_to_si_string)[](#RsInstrument.value_to_si_string "Link to this definition")
:   Returns the entered float value converted to string with SI notation.
    :param value: input float value
    :param fmt: formatting of the number. Default: ‘.12g’
    :param min\_decimal\_places: assures minimal number of decimal places.
    If you set the number > 0, the function makes sure the decimal places are kept, and
    if there are less of them, they are filled with nulls (‘.000’ or ‘000’) Default: 0
    .. rubric:: Examples

    * value = 1, fmt = ‘.12g’, min\_decimal\_places = 0, result -> ‘1’
    * value = 1, fmt = ‘.12g’, min\_decimal\_places = 3, result -> ‘1.000’

    Parameters:
    :   **str\_after\_number** – string after number, if the SI suffix is present. Default: ‘ ‘

    Examples

    * 1.23 -> ‘1.23’
    * 1.23E3 -> ‘1.23 k’
    * 2.56E9 -> ‘2.56 G’
    * 11.3E-6 -> ‘-11.3 u’

    This function is useful for user-readable string outputs.