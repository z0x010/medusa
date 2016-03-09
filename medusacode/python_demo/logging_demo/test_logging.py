#!/usr/bin/env python
# coding:utf-8

import logging
import sys


# Logger
"""
logging.getLogger([name])
    Return a logger with the specified name
    or, if no name is specified, return a logger which is the root logger of the hierarchy.
    If specified, the name is typically a dot-separated hierarchical name like “a”, “a.b” or “a.b.c.d”.
    Choice of these names is entirely up to the developer who is using logging.

    All calls to this function with a given name return the same logger instance.
    This means that logger instances never need to be passed between different parts of an application.
"""
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)


# Handler
"""
The StreamHandler class, located in the core logging package, sends logging output to streams
such as sys.stdout, sys.stderr or any file-like object
(or, more precisely, any object which supports write() and flush() methods).

class logging.StreamHandler(stream=None)
    Returns a new instance of the StreamHandler class.
    If stream is specified, the instance will use it for logging output;
    otherwise, sys.stderr will be used.
"""
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(logging.INFO)

"""
The FileHandler class, located in the core logging package, sends logging output to a disk file.
It inherits the output functionality from StreamHandler.

class logging.FileHandler(filename, mode='a', encoding=None, delay=False)
    Returns a new instance of the FileHandler class.
    The specified file is opened and used as the stream for logging.
    If mode is not specified, 'a' is used.
    If encoding is not None, it is used to open the file with that encoding.
    If delay is true, then file opening is deferred until the first call to emit().
    By default, the file grows indefinitely.
"""
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.INFO)

# Why are there two setLevel() methods?
# The level set in the logger determines which severity of messages it will pass to its handlers.
# The level set in each handler determines which messages that handler will send on.


# Formatter
formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(processName)s %(thread)d %(threadName)s [%(message)s]')


"""
usage:
Handler.setFormatter(formatter)
Logger.addHandler(handler)
"""
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(stream_handler)  # A logger can have multiple handlers
logger.addHandler(file_handler)  # A logger can have multiple handlers




logger.debug('test debug')
logger.info('test info')
logger.warning('test warning')
logger.error('test error')
logger.critical('test critical')
