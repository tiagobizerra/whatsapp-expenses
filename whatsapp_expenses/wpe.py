#!/usr/local/bin/python

'''
WhatsApp Expenses Modules
'''

import logging
import platform
import sys
from report import check_report_file, build_report, build_expense_report

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
    WhatsApp expenses Function
    '''

    check_report_file(filename)
    build_report(filename)
