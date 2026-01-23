# RsInstrument.logger

> Source: https://rsinstrument.readthedocs.io/en/latest/logger.html

# RsInstrument.logger[](#rsinstrument-logger "Link to this heading")

Check the usage in the Getting Started chapter [Logging](StepByStepGuide.html#gettingstarted-logging).

*class* ScpiLogger[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger "Link to this definition")
:   Base class for SCPI logging

    mode[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.mode "Link to this definition")
    :   Sets the logging ON or OFF. Additionally, you can set the logging ON only for errors.
        Possible values:

        * LoggingMode.Off - logging is switched OFF
        * LoggingMode.On - logging is switched ON
        * LoggingMode.Errors - logging is switched ON, but only for error entries
        * LoggingMode.Default - sets the logging to default - the value you have set with logger.default\_mode

    stop() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.stop)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.stop "Link to this definition")
    :   Stops the logging. This is the same as: mode = LoggingMode.Off

    start() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.start)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.start "Link to this definition")
    :   Starts the logging with the last defined LoggingMode. Default is LoggingMode.On

    default\_mode[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.default_mode "Link to this definition")
    :   Sets / returns the default logging mode.
        You can recall the default mode by calling the ‘logger.mode = LoggingMode.Default’.

    device\_name*: str*[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.device_name "Link to this definition")
    :   Use this property to change the resource name in the log from the default Resource Name (e.g. TCPIP::192.168.2.101::INSTR)
        to another name e.g. ‘MySigGen1’.

    set\_logging\_target(*target*, *console\_log: bool | None = None*, *udp\_log: bool | None = None*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.set_logging_target)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.set_logging_target "Link to this definition")
    :   Sets local logging stream target - the target must implement write() and flush().
        You can optionally set the console and UDP logging ON or OFF.
        This method switches the logging target global to OFF.

    get\_logging\_target()[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.get_logging_target)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.get_logging_target "Link to this definition")
    :   Based on the global\_mode, it returns the logging target: either the local or the global one.

    set\_logging\_target\_global(*console\_log: bool | None = None*, *udp\_log: bool | None = None*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.set_logging_target_global)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.set_logging_target_global "Link to this definition")
    :   Sets logging target to global. The global target must be defined.
        You can optionally set the console and UDP logging ON or OFF.
        This method switches the logging target global to ON.

    log\_to\_console[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.log_to_console "Link to this definition")
    :   Returns logging to console status.

    log\_to\_udp[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.log_to_udp "Link to this definition")
    :   Returns logging to UDP status.

    log\_to\_console\_and\_udp[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.log_to_console_and_udp "Link to this definition")
    :   Returns true, if both logging to UDP and console in are True.

    info\_raw(*log\_entry: str*, *add\_new\_line: bool = True*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.info_raw)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.info_raw "Link to this definition")
    :   Method for logging the raw string without any formatting.

    info(*start\_time: datetime | float | None*, *end\_time: datetime | float | None*, *log\_string\_info: str*, *log\_string: str*, *cmd: str | None = None*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.info)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.info "Link to this definition")
    :   Method for logging one info entry. For binary log\_string, use the info\_bin()

    error(*start\_time: datetime | float | None*, *end\_time: datetime | float | None*, *log\_string\_info: str*, *log\_string: str*, *cmd: str | None = None*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.error)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.error "Link to this definition")
    :   Method for logging one error entry.

    set\_relative\_timestamp(*timestamp: datetime*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.set_relative_timestamp)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.set_relative_timestamp "Link to this definition")
    :   If set, the further timestamps will be relative to the entered time.

    set\_relative\_timestamp\_now() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.set_relative_timestamp_now)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.set_relative_timestamp_now "Link to this definition")
    :   Sets the relative timestamp to the current time.

    get\_relative\_timestamp() → datetime | None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.get_relative_timestamp)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.get_relative_timestamp "Link to this definition")
    :   Based on the global\_mode, it returns the relative timestamp: either the local or the global one.

    clear\_relative\_timestamp() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.clear_relative_timestamp)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.clear_relative_timestamp "Link to this definition")
    :   Clears the reference time, and the further logging continues with absolute times.

    set\_time\_offset\_zero\_on\_first\_entry() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.set_time_offset_zero_on_first_entry)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.set_time_offset_zero_on_first_entry "Link to this definition")
    :   Sets the reference time to the value of the first log entry start time.
        This effectively means, the log is guaranteed to start with “00:00:00.000” start time.

    flush() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.flush)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.flush "Link to this definition")
    :   Flush all the entries.

    sync\_from(*source: [ScpiLogger](#RsInstrument.Internal.ScpiLogger.ScpiLogger "RsInstrument.Internal.ScpiLogger.ScpiLogger")*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.sync_from)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.sync_from "Link to this definition")
    :   Synchronises this Logger with the source logger.

    log\_status\_check\_ok[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.log_status_check_ok "Link to this definition")
    :   Sets / returns the current status of status checking OK.
        If True (default), the log contains logging of the status checking ‘Status check: OK’.
        If False, the ‘Status check: OK’ is skipped - the log is more compact.
        Errors will still be logged.

    clear\_cached\_entries() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.clear_cached_entries)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.clear_cached_entries "Link to this definition")
    :   Clears potential cached log entries.
        Cached log entries are generated when the Logging is ON, but no target has been defined yet.

    set\_format\_string(*value: str*, *line\_divider: str = '\n'*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.set_format_string)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.set_format_string "Link to this definition")
    :   Sets new format string and line divider.
        If you just want to set the line divider, set the format string value=None
        The original format string is: `PAD_LEFT12(%START_TIME%) PAD_LEFT25(%DEVICE_NAME%) PAD_LEFT12(%DURATION%)  %LOG_STRING_INFO%: %LOG_STRING%`

        Additional variables to use: `%SCPI_COMMAND%`.

    restore\_format\_string() → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#ScpiLogger.restore_format_string)[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.restore_format_string "Link to this definition")
    :   Restores the original format string and the line divider to LF

    abbreviated\_max\_len\_ascii*: int*[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.abbreviated_max_len_ascii "Link to this definition")
    :   Defines the maximum length of one ASCII log entry. Default value is 200 characters.

    abbreviated\_max\_len\_bin*: int*[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.abbreviated_max_len_bin "Link to this definition")
    :   Defines the maximum length of one Binary log entry. Default value is 2048 bytes.

    abbreviated\_max\_len\_list*: int*[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.abbreviated_max_len_list "Link to this definition")
    :   Defines the maximum length of one list entry. Default value is 100 elements.

    bin\_line\_block\_size*: int*[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.bin_line_block_size "Link to this definition")
    :   Defines number of bytes to display in one line. Default value is 16 bytes.

    udp\_port[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.udp_port "Link to this definition")
    :   Returns udp logging port.

    target\_auto\_flushing[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.target_auto_flushing "Link to this definition")
    :   Returns status of the auto-flushing for the logging target.

    log\_info\_replacer*: [LogInfoReplacer](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer "RsInstrument.Internal.ScpiLogger.LogInfoReplacer")*[](#RsInstrument.Internal.ScpiLogger.ScpiLogger.log_info_replacer "Link to this definition")
    :   Replacer for Log Info Strings.

*class* LogInfoReplacer[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer "Link to this definition")
:   Replacer, that takes the SCPI Logger Log Info and customizes its value.

    Create the new LogInfoReplacer either with empty replacer dictionaries,
    or the ones from another LogInfoReplacer.

    set\_full\_replacer(*repl\_dict: Dict[str, str]*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.set_full_replacer)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.set_full_replacer "Link to this definition")
    :   Sets the full-replacer dictionary.
        This replacer searches the dictionary (case-sensitive) for the key
        that equals the LogInfoString, and replaces the whole info string
        with the string value associated with that key.

    put\_full\_replacer\_item(*match: str*, *replace: str*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.put_full_replacer_item)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.put_full_replacer_item "Link to this definition")
    :   Sets/replaces one item in the full replacer.

    pop\_full\_replacer\_item(*match: str*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.pop_full_replacer_item)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.pop_full_replacer_item "Link to this definition")
    :   Pops(removes) the entered full replacer item.

    set\_regex\_sr\_replacer(*repl\_dict: Dict[Pattern, str]*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.set_regex_sr_replacer)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.set_regex_sr_replacer "Link to this definition")
    :   Sets the regex search&replace replacer dictionary. The replacer uses the re.sub() method
        of each key and replaces the matched substring with the string value associated with that key.

    put\_regex\_sr\_replacer\_item(*search: Pattern | str*, *replace: str*) → Pattern[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.put_regex_sr_replacer_item)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.put_regex_sr_replacer_item "Link to this definition")
    :   Sets/replaces one item in the regex replacer. The key can be either a regex pattern,
        or a string. In case of the string, the key is compiled to a regex pattern,
        before it is put into the replacing dictionary.
        Returns the resulting search regex pattern.

    pop\_regex\_sr\_replacer\_item(*search: Pattern | str*) → None[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.pop_regex_sr_replacer_item)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.pop_regex_sr_replacer_item "Link to this definition")
    :   Pops(removes) the entered regex replacer item. The key can be either a regex pattern,
        or a string. In case of the string, the key is compiled to a regex pattern prior to popping.

    clear\_replacers()[[source]](_modules/RsInstrument/Internal/ScpiLogger.html#LogInfoReplacer.clear_replacers)[](#RsInstrument.Internal.ScpiLogger.LogInfoReplacer.clear_replacers "Link to this definition")
    :   Clears both full and regex replacer dictionaries.