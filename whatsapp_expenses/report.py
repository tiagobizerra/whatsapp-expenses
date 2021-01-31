#!/usr/local/bin/python

'''
Report functions
'''

import logging
import os
import sys
from expenses import create_expense, validate_expense

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

def check_report_file(filename):

    '''
    Check report file
    '''

    logging.info('Reading file %s', filename)
    try:
        os.path.exists(filename)
        os.path.isfile(filename)
    except IOError as err:
        logging.error('Error loading file %s\n%s', filename, err)
        sys.exit(1)

def build_report(filename):

    '''
    Function to build report based on file
    '''

    valid_expenses = 0
    invalid_expenses = 0

    wpe_filename = open(filename)
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

            logging.info('Reading report from previous expense')
            expense = line.split(' ')

            if bool(validate_expense(expense)) is True:

                logging.info('Valid! Creating expense: %s', expense)
                valid_expenses += 1
                create_expense(expense)

            else:
                logging.info('Invalid! Skipping expense: %s', expense)
                invalid_expenses += 1

    wpe_filename.close()
