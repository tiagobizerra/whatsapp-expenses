#!/usr/local/bin/python3

'''
WhatsApp Expenses Modules
'''

import logging
import platform
import sys

class HostnameFilter(logging.Filter):

    '''
    Logging
    '''

    hostname = platform.node()

    def filter(self, record):
        record.hostname = HostnameFilter.hostname
        return True

HANDLER = logging.StreamHandler(sys.stdout)
HANDLER.addFilter(HostnameFilter())
HANDLER.setFormatter(
    logging.Formatter(
        "%(asctime)s %(hostname)s - whatsapp expenses - %(levelname)s : %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%Sz",
    )
)

LOGGER = logging.getLogger()
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)


def wpefile(filename):

    '''
    Main Function
    '''

    logging.info('Reading file %s', filename)
    try:
        wpe_filename = open(filename)
    except IOError as err:
        logging.error('File not found: %s\n%s', filename, err)

    print(wpe_filename)
