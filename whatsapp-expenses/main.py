'''
WhatsApp expenses
'''
#!/usr/loca/bin/python3

import argparse
import os.path
from wpe import wpe

'''
Argument parser
'''

parser = argparse.ArgumentParser(
    description='Calculates expenses based on an exported WhatsApp channel history')

parser.add_argument('-f', dest="filename", required=True, metavar='--file',
    help='WhatsApp channel history file')

args = parser.parse_args()

wpe(args.filename)