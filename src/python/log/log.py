# -*- coding:utf-8 -*-

import os
import logging
import logging.config
import threading


_logger = None
_logger_lock = threading.Lock()

def from_file(logger='', filename=None):
    '''Parse log config from file.

    Precedence: env['LOG_CONF'] > filename parameter > default conf
    '''
    conf_env_key = 'LOG_CONF'
    if conf_env_key in os.environ:
        filename = os.environ[conf_env_key]
    elif filename:
        pass
    else:
        filename = 'conf/logging.conf'
    logging.config.fileConfig(filename)
    logging.info('logging init')


from_file()
log = logging.getLogger('nre')


if __name__ == "__main__":
    log = logging.getLogger('rootx')
    log.error("this is an error test")
    log.warn("this is a warn test")
    log.info("this is a info test")
    log.debug("this is a debug test")
