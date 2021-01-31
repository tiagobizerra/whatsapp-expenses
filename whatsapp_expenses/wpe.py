#!/usr/local/bin/python

'''
WhatsApp Expenses Modules
'''

import logging
import platform
import sys
from expenses import create_expense, validate_expense

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

def create_report_metadata(metadata):

    '''
    Generate metadata for a new expense from string passed
    Metadata returned as a dict includes: date, time, user
    '''

    raw_metadata = metadata.split(' ')[0:3]

    report_metadata = {
            "date": raw_metadata[0][1:-1],
            "time": raw_metadata[1].replace(']',''),
            "user": raw_metadata[2].replace(':','')
        }

    return report_metadata


def wpefile(filename):

    '''
    Main Function
    '''

    valid_expenses = 0
    invalid_expenses = 0

    logging.info('Reading file %s', filename)
    try:
        wpe_filename = open(filename)
    except IOError as err:
        logging.error('File not found: %s\n%s', filename, err)

    lines = wpe_filename.readlines()
    count = 0

    for line in lines:

        count += 1

        if line.startswith('['):

            logging.info('New expense! Creating report metadata')
            report_metadata = create_report_metadata(line)
            logging.info(report_metadata)

            expense = line.split(' ')[3:]
            expense[-1] = expense[-1].rstrip("\n")

            logging.info('Checking if expense is valid: %s', expense)

            if bool(validate_expense(expense)) is True:

                logging.info('Valid! Creating expense: %s', expense)
                valid_expenses += 1
                create_expense(expense)

            else:
                logging.info('Invalid! Skipping expense: %s', expense)
                invalid_expenses += 1

        else:

            logging.info('Previous')
            expense = line.split(' ')

            if bool(validate_expense(expense)) is True:

                logging.info('Valid! Creating expense: %s', expense)
                valid_expenses += 1
                create_expense(expense)

            else:
                logging.info('Invalid! Skipping expense: %s', expense)
                invalid_expenses += 1

    wpe_filename.close()
