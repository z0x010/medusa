#!/usr/bin/env python
# coding:utf-8

import logging
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # loggers
    'loggers': {
        'test_logger': {
            'level': 'DEBUG',
            'propagate': True,
            'filters': [],
            'handlers': ['test_handler'],
        }
    },
    # handlers
    'handlers': {
        'test_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'test_formatter',
            'filters': [],
        },
    },
    # filters
    'filters': {
        'test_filter': {
        }
    },
    # formatters
    'formatters': {
        'test_formatter': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d [%(message)s]',
        }
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('test_logger')

def func(a, b):
    try:
        ret = a/b
        logger.info(ret)
        return ret
    except Exception, e:
        logger.warning('%s : %s' % (type(e), e))
        pass
    pass

print func(9, 1)
print func(1, 0)
