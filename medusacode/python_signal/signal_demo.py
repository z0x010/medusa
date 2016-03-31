#!/usr/bin/env python
# coding:utf-8

"""
signal — Set handlers for asynchronous events
"""
"""
signal.signal(signalnum, handler)
    Set the handler for signal signalnum to the function handler.
    handler can be a callable Python object taking two arguments (see below),
    or one of the special values signal.SIG_IGN or signal.SIG_DFL.
    The previous signal handler will be returned.

    When threads are enabled, this function can only be called from the main thread;
    attempting to call it from other threads will cause a ValueError exception to be raised.

    The handler is called with two arguments:
        the signal number
        the current stack frame (None or a frame object;

signal.pause()
    Cause the process to sleep until a signal is received;
    the appropriate handler will then be called.
    Returns nothing.


signal.getsignal(signalnum)
    Return the current signal handler for the signal signalnum.
    The returned value may be a callable Python object, or one of the special values:
        signal.SIG_IGN(1),
        signal.SIG_DFL(0),
        None.
    signal.SIG_IGN means that the signal was previously ignored,
    signal.SIG_DFL means that the default way of handling the signal was previously in use,
    None means that the previous signal handler was not installed from Python.

"""

import signal
import os

print signal.getsignal(signal.SIGKILL)
# None
print signal.getsignal(signal.SIGTERM)
# 0
print signal.getsignal(signal.SIGTSTP)
# 0

def handler(signal_number, stack_frame):
    print '(received signal)', signal_number
    print '(stack_frame)', stack_frame

print 'pid', os.getpid()
# signal.signal(signal.SIGKILL, handler)  # 9
signal.signal(signal.SIGTERM, handler)  # 15
signal.signal(signal.SIGTSTP, handler)  # 18
signal.pause()
