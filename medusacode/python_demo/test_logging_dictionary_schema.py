#!/usr/bin/env python
# coding:utf-8

import logging
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'test_formatter': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d [%(message)s]',
        }
    },
    'filters': {
        'test_filter': {
        }
    },
    'handlers': {
        'test_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': ['test_formatter'],
            'filters': [],
        },
    },
    'loggers': {
        'test_logger': {
            'level': 'DEBUG',
            'propagate': True,
            'filters': [],
            'handlers': ['test_handler'],
        }
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('test_logger')

def func(a, b):
    try:
        ret = a/b
        logger.info(ret)
        return ret
    except Exception, e:
        logger.warning(e)
        pass
    pass

print func(1, 2)
print func(2, 0)
