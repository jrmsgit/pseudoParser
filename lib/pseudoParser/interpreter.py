import json
from . import vartypes, commands

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def runprog(program):
    print()
    print("*******************************************************")
    print(json.dumps(program, indent=2, sort_keys=True))
    print("*******************************************************")
    print()


    for lineno in sorted(program.keys()):
        stat = program[lineno]
        _dbg("%s:" % lineno, stat)

        if stat[0] == 'DECLARE':
            vartypes.declare(stat[1], stat[2])

        elif stat[0] == 'ASSIGN':
            vartypes.assign(stat[1], stat[2])

        elif stat[0] == 'INIT':
            vartypes.iniciar(stat[2])

        elif stat[0] == 'COMMAND':
            args = list()
            for a in stat[2]:
                if vartypes.isDeclared(a):
                    args.append(vartypes.getVar(a))
                else:
                    args.append(a)
            commands.run(stat[1], args)


    print()
    print("*******************************************************")
    print(vartypes.varsTableRepr())
    print("*******************************************************")
    print()
