#!/usr/bin/python3
# Stolen from: http://www.dabeaz.com/ply/example.html

from .parser import *

import sys
try:
    fh = open(sys.argv[1], 'r')
    parser.parse(fh.read())
    fh.close()
except IndexError:
    parser.parse(sys.stdin.read())

print()
print("*******************************************************")
print()
print(namesTable)
