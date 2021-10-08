#!/usr/local/bin/python

'''
Report functions
'''

import logging
import os
import sys
from categories import check_category
from expenses import create_expense, create_expense_files, validate_expense, write_expense


def list_to_string(list_to_convert):

    '''
    Convert a list into a string
    '''

    final_string = " ".join(str(item) for item in list_to_convert)

    return (final_string)


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
    Function to build report files based on whatsapp chat file
    '''

    expense_files = create_expense_files()

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

            raw_expense = line.split(' ')[3:]
            raw_expense[-1] = raw_expense[-1].rstrip("\n")

            expense = list_to_string(raw_expense)
            print(expense)

            logging.info('Checking if expense is valid: %s', expense)

            if bool(validate_expense(expense)) is True:

                logging.info('Valid! Creating expense: %s', expense)
                valid_expenses += 1
                create_expense(expense)
                write_expense(expense, True, expense_files)

            else:
                logging.info('Invalid! Skipping expense: %s', expense)
                invalid_expenses += 1
                write_expense(expense, False, expense_files)

        else:

            logging.info('Reading expense info from previous report')
            expense = str(line.rstrip("\n"))

            if bool(validate_expense(expense)) is True:

                logging.info('Valid! Creating expense: %s', expense)
                valid_expenses += 1
                create_expense(expense)
                write_expense(expense, True, expense_files)

            else:
                logging.info('Invalid! Skipping expense: %s', expense)
                invalid_expenses += 1
                write_expense(expense, False, expense_files)

    wpe_filename.close()

    build_expense_report(expense_files)

def build_expense_report(expense_files):

    '''
    Build expense report
    '''

    logging.info('Reading file %s', expense_files[0])
    try:
        os.path.exists(expense_files[0])
        os.path.isfile(expense_files[0])
    except IOError as err:
        logging.error('Error loading file %s\n%s', expense_files[0], err)
        sys.exit(1)

    #print(expense_files)

    valid_expenses = open(expense_files[0])
    lines = valid_expenses.readlines()
    count = 0
    cost_total = 0.0
    
    for line in lines:

        count += 1
        expense=line.split()
        print(expense)
        category = str(check_category(str.lower(expense[1])))
        cost = float(expense[0].replace("," , "."))
        cost_total =+ cost_total + cost 

    print(cost_total)
    return expense_files
