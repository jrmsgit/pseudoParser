#!/usr/bin/python3
# Initially stolen from: http://www.dabeaz.com/ply/example.html

import sys
from .parser import *

try:
    fh = open(sys.argv[1], 'r')
    for codeLine in fh.readlines():
        parser.parse(codeLine)
    fh.close()
except IndexError:
    for codeLine in sys.stdin.readlines():
        parser.parse(codeLine)

print()
print("*******************************************************")
print()
print(vartypes.varsTableRepr())
print()
print("*******************************************************")
print()
