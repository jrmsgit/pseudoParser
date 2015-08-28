#!/usr/bin/python3
# Initially stolen from: http://www.dabeaz.com/ply/example.html

import sys

from .parser import parser
from .interpreter import runprog

code = None
try:
    fh = open(sys.argv[1], 'r')
    code = fh.read()
    fh.close()
except IndexError:
    code = sys.stdin.read()

program = parser.parse(code)
runprog(program)
