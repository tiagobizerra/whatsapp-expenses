#!/usr/local/bin/python

'''
Expenses functions
'''

import logging
import os
import re
import sys

def format_expense(raw_expense):

    '''
    Format a expense
    '''

    return None

def validate_expense(expense_string):

    '''
    Validate a expense
    '''

    if re.match('^\\d+\\s', expense_string) or re.match('^\\d+(\\.|\\,)\\d+\\s', expense_string):
        return True

    if re.match('^\\D+\\s', expense_string) and re.match('\\s\\d+(\\.|\\,)\\d+$', expense_string):
        return True

    return False

def create_expense(expense):

    '''
    Create a new expense from string passed
    '''

    for data in expense:
        new_expense = {
                'cost': data[0],
                'name': data[1:]
            }

    return new_expense

def create_expense_files():

    '''
    Create files to report expenses
    Returns both valid_expense_file and invalid_expense_file
    '''
    data_dir = os.path.dirname(os.path.abspath(__file__)) + "/data/"

    valid_expense_file = data_dir + "valid_expenses.txt"
    invalid_expense_file = data_dir + "invalid_expenses.txt"

    if os.path.isfile(valid_expense_file):
        logging.error('file %s exists', valid_expense_file)
        sys.exit(1)
    else:
        with open(valid_expense_file, 'w') as create_file:
            #create_file.write("Valid Expenses\n")
            pass

    if os.path.isfile(invalid_expense_file):
        logging.error('file %s exists', invalid_expense_file)
        sys.exit(1)
    else:
        with open(invalid_expense_file, 'w') as create_file:
            #create_file.write("Invalid Expenses\n")
            pass

    return(valid_expense_file, invalid_expense_file)

def write_expense(expense, is_valid, expense_files):

    '''
    Write expense to file based on validation and expense files passed
    '''

    if is_valid is True:
        with open(expense_files[0], 'a') as expense_file:
            expense_file.write(str(expense) + '\n')
    else:
        with open(expense_files[1], 'a') as expense_file:
            expense_file.write(str(expense) + '\n')
