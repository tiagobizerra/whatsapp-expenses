#!/usr/local/bin/python

'''
Expenses functions
'''

def format_expense(raw_expense):

    '''
    Format a expense
    '''

    return None

def validate_expense(formated_expense):

    '''
    Validate a expense
    '''

    if len(formated_expense) == 2 and (formated_expense[0] and formated_expense[1]):
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
