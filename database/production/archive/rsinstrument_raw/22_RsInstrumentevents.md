# RsInstrument.events

> Source: https://rsinstrument.readthedocs.io/en/latest/events.html

# RsInstrument.events[](#rsinstrument-events "Link to this heading")

*class* Events[[source]](_modules/RsInstrument/Fixed_Files/Events.html#Events)[](#RsInstrument.Fixed_Files.Events.Events "Link to this definition")
:   Common Events class.
    Event-related methods and properties. Here you can set all the event handlers.

    *property* before\_query\_handler*: Callable*[](#RsInstrument.Fixed_Files.Events.Events.before_query_handler "Link to this definition")
    :   Returns the handler of before\_query events.

        Returns:
        :   current `before_query_handler`

    *property* before\_write\_handler*: Callable*[](#RsInstrument.Fixed_Files.Events.Events.before_write_handler "Link to this definition")
    :   Returns the handler of before\_write events.

        Returns:
        :   current `before_write_handler`

    *property* io\_events\_include\_data*: bool*[](#RsInstrument.Fixed_Files.Events.Events.io_events_include_data "Link to this definition")
    :   Returns the current state of the io\_events\_include\_data See the setter for more details.

    *property* on\_read\_handler*: Callable*[](#RsInstrument.Fixed_Files.Events.Events.on_read_handler "Link to this definition")
    :   Returns the handler of on\_read events.

        Returns:
        :   current `on_read_handler`

    *property* on\_write\_handler*: Callable*[](#RsInstrument.Fixed_Files.Events.Events.on_write_handler "Link to this definition")
    :   Returns the handler of on\_write events.

        Returns:
        :   current `on_write_handler`

    sync\_from(*source: [Events](#RsInstrument.Fixed_Files.Events.Events "RsInstrument.Fixed_Files.Events.Events")*) → None[[source]](_modules/RsInstrument/Fixed_Files/Events.html#Events.sync_from)[](#RsInstrument.Fixed_Files.Events.Events.sync_from "Link to this definition")
    :   Synchronises these Events with the source.