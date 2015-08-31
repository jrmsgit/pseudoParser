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
testscount = 0
testsfail = 0

def checkStatements(stats):
    global testsfail
    if interpreter.statements == stats:
        print("PASS")
    else:
        print("FAIL")
        print("GOT:")
        print(yaml.dump(interpreter.statements))
        print("EXPECT:")
        print(yaml.dump(stats))
        testsfail += 1

for testFile in sorted(glob.glob(mydir+"/*.yml")):
    curtfile = os.path.basename(testFile)[:-4]
    with open(testFile, 'r') as fh:
        tests = yaml.load(fh.read())
        fh.close()
        for t in tests:
            curtname = t['name']
            testscount += 1
            print('TEST:%s' % curtfile, curtname)
            try:
                program = compiler.parser.parse(t['code'])
                interpreter.runprog(program)
            except Exception as e:
                print('FAIL:%s' % curtfile, curtname)
                print('EXCEPTION:', e)
                testsfail += 1
            else:
                checkStatements(t['statements'])
            print()

print(testscount, 'tests run,', testsfail, 'failed')
