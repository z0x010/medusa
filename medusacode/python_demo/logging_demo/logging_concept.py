# coding=utf-8

"""
A Python logging configuration consists of four parts:
    Loggers
    Handlers
    Filters
    Formatters
"""

"""
Loggers

    A logger is the entry point into the logging system.
    Each logger is a named bucket to which messages can be written for processing.

    A logger is configured to have a log level.
    This log level describes the severity of the messages that the logger will handle.
    Python defines the following log levels:
        DEBUG: Low level system information for debugging purposes
        INFO: General system information
        WARNING: Information describing a minor problem that has occurred.
        ERROR: Information describing a major problem that has occurred.
        CRITICAL: Information describing a critical problem that has occurred.

    Each message that is written to the logger is a Log Record.
    Each log record also has a log level indicating the severity of that specific message.
    A log record can also contain useful metadata that describes the event that is being logged.
    This can include details such as a stack trace or an error code.

    When a message is given to the logger, the log level of the message is compared to the log level of the logger.
    If the log level of the message meets or exceeds the log level of the logger itself,
    the message will undergo further processing. If it doesn’t, the message will be ignored.

    Once a logger has determined that a message needs to be processed, it is passed to a Handler.
"""

"""
Handlers

    The handler is the engine that determines what happens to each message in a logger.
    It describes a particular logging behavior, such as writing a message to the screen, to a file, or to a network socket.

    Like loggers, handlers also have a log level.
    If the log level of a log record doesn’t meet or exceed the level of the handler, the handler will ignore the message.

    A logger can have multiple handlers, and each handler can have a different log level.
    In this way, it is possible to provide different forms of notification depending on the importance of a message.
    For example, you could install one handler that forwards ERROR and CRITICAL messages to a paging service,
    while a second handler logs all messages (including ERROR and CRITICAL messages) to a file for later analysis.
"""

"""
Filters

    A filter is used to provide additional control over which log records are passed from logger to handler.

    By default, any log message that meets log level requirements will be handled.
    However, by installing a filter, you can place additional criteria on the logging process.
    For example, you could install a filter that only allows ERROR messages from a particular source to be emitted.

    Filters can also be used to modify the logging record prior to being emitted.
    For example, you could write a filter that downgrades ERROR log records to WARNING records
    if a particular set of criteria are met.

    Filters can be installed on loggers or on handlers;
    multiple filters can be used in a chain to perform multiple filtering actions.
"""

"""
Formatters

    Ultimately, a log record needs to be rendered as text.
    Formatters describe the exact format of that text.
    A formatter usually consists of a Python formatting string;
    however, you can also write custom formatters to implement specific formatting behavior.
"""
