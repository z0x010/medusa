#!/usr/bin/env python
# coding:utf-8

import logging
import sys

logger = logging.getLogger('test_log')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler(stream=sys.stdout)
# sh.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')
# fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(processName)s %(thread)d %(threadName)s %(message)s')
sh.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(sh)
logger.addHandler(fh)

logger.info('test logger')
