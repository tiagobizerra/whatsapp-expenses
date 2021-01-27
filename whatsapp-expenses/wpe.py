#!/usr/loca/bin/python3

def wpe(file):

    try:
        f = open(file)
    except IOError:
        print("File not found")