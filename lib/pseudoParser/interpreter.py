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


    def cmdStat(stat):
        args = list()
        for a in stat[2]:
            args.append(evalExpr(a))
        return commands.run(stat[1], args)


    def evalExpr(expr):
        _dbg('evalExpr:', expr)
        if vartypes.isDeclared(expr):
            # ID expression
            return vartypes.getVar(expr)
        elif isinstance(expr, tuple):
            if expr[0] == 'COMMAND':
                # command expression
                return cmdStat(expr)
        else:
            # constant expression
            return expr


    for lineno in sorted(program.keys()):
        stat = program[lineno]
        _dbg("%s:" % lineno, stat)

        if stat[0] == 'DECLARE':
            vartypes.declare(stat[1], stat[2])

        elif stat[0] == 'ASSIGN':
            vartypes.assign(stat[1], evalExpr(stat[2]))

        elif stat[0] == 'INIT':
            vartypes.iniciar(stat[2])

        elif stat[0] == 'COMMAND':
            cmdStat(stat)


    print()
    print("*******************************************************")
    print(vartypes.varsTableRepr())
    print("*******************************************************")
    print()
