#!/usr/bin/env python
# coding:utf-8

import logging
import sys

# Logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

# Handler
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)
"""
Why are there two setLevel() methods?
The level set in the logger determines which severity of messages it will pass to its handlers.
The level set in each handler determines which messages that handler will send on.
"""

# Formatter
formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(processName)s %(thread)d %(threadName)s %(message)s')

"""
Handler.setFormatter(formatter)
Logger.addHandler(handler)
"""
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('test debug')
logger.info('test info')
logger.warning('test warning')
logger.error('test error')
logger.critical('test critical')
