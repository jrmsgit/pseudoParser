#!/usr/bin/python3
# Initially stolen from: http://www.dabeaz.com/ply/example.html

from .parser import *

import sys
try:
    fh = open(sys.argv[1], 'r')
    for codeLine in fh.readlines():
        parser.parse(codeLine.strip())
    fh.close()
except IndexError:
    for codeLine in sys.stdin.readlines():
        parser.parse(codeLine.strip())

print()
print("*******************************************************")
print()
print(varsTable)
print()
print("*******************************************************")
print()
