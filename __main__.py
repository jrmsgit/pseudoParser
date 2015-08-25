#!/usr/bin/python3
# Initially stolen from: http://www.dabeaz.com/ply/example.html

from .parser import *

import sys
try:
    fh = open(sys.argv[1], 'r')
    parser.parse(fh.read().strip())
    fh.close()
except IndexError:
    parser.parse(sys.stdin.read().strip())

print()
print("*******************************************************")
print()
print(varsTable)
