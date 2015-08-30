import sys
import os.path
import yaml
import glob

mydir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(mydir, '..', 'lib'))

from pseudoParser import compiler
from pseudoParser import interpreter

curtfile = None
curtname = None

def checkStatements(stats):
    if interpreter.statements == stats:
        print("PASS:%s" % curtfile, curtname)
    else:
        print("FAIL:%s" % curtfile, curtname)
        print("GOT:")
        print(yaml.dump(interpreter.statements))
        print("EXPECT:")
        print(yaml.dump(stats))

for testFile in sorted(glob.glob(mydir+"/*.yml")):
    curtfile = os.path.basename(testFile)[:-4]
    with open(testFile, 'r') as fh:
        tests = yaml.load(fh.read())
        fh.close()
        for t in tests:
            curtname = t['name']
            #~ print('TEST:%s' % curtfile, curtname)
            try:
                program = compiler.parser.parse(t['code'])
                interpreter.runprog(program)
            except Exception as e:
                print('FAIL:%s' % curtfile, curtname)
                print('EXCEPTION:', e)
            else:
                checkStatements(t['statements'])
