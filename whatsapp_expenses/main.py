#!/usr/local/bin/python3
'''
WhatsApp expenses
Calculates your expenses based on information sent to an exported WhatsApp channel
'''

import argparse
from wpe import wpefile

PARSER = argparse.ArgumentParser(
    description='Calculates expenses based on an exported WhatsApp channel history')

PARSER.add_argument('-f', dest="filename", required=True, metavar='--filename',
                    help='WhatsApp channel history file')

ARGS = PARSER.parse_args()

wpefile(ARGS.filename)
