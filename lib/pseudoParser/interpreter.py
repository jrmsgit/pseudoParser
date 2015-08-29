import json
from . import vartypes, commands
from .logger import ppLogger

logger = ppLogger(__name__)

def runprog(program):
    print()
    print("*******************************************************")
    print(json.dumps(program, indent=2, sort_keys=True))
    print("*******************************************************")
    print()


    def cmdStat(stat):
        logger.dbg('cmdStat:', stat)
        args = list()
        for a in stat[2]:
            args.append(evalExpr(a))
        return commands.run(stat[1], args)


    def evalStat(stat):
        if stat[0] == 'DECLARE':
            vartypes.declare(stat[1], stat[2])

        elif stat[0] == 'ASSIGN':
            vartypes.assign(stat[1], evalExpr(stat[2]))

        elif stat[0] == 'INIT':
            vartypes.iniciar(stat[2])

        elif stat[0] == 'COMMAND':
            cmdStat(stat)

        elif stat[0] == 'CONDSTAT':
            condStat(stat)

        elif stat[0] == 'LOOPSTAT':
            loopStat(stat)


    def evalExpr(expr):
        if isinstance(expr, tuple):
            logger.dbg('evalExpr:', str(expr))
            for expr2 in expr:
                evalStat(expr2)

        elif vartypes.isDeclared(expr):
            # ID expression
            logger.dbg('evalExpr ID:', expr)
            return vartypes.getVar(expr).getVal()

        else:
            # constant expression
            logger.dbg('evalExpr constant:', expr)
            return expr


    def evalCompExpr(expr):
        logger.dbg('evalCompExpr:', expr)
        if expr[1] == '==': return evalExpr(expr[0]) == evalExpr(expr[2])
        if expr[1] == '!=': return evalExpr(expr[0]) != evalExpr(expr[2])
        if expr[1] == '>': return evalExpr(expr[0]) > evalExpr(expr[2])
        if expr[1] == '>=': return evalExpr(expr[0]) >= evalExpr(expr[2])
        if expr[1] == '<': return evalExpr(expr[0]) < evalExpr(expr[2])
        if expr[1] == '<=': return evalExpr(expr[0]) <= evalExpr(expr[2])


    def condStat(stat):
        logger.dbg('condStat:', stat)
        cond = stat[1][0]
        if cond == 'IF':
            comp = stat[1][1]
            expr = stat[1][2]
            if evalCompExpr(comp): return evalExpr(expr)
            else: return False


    def loopStat(stat):
        logger.dbg('loopStat:', stat)
        loop = stat[1][0]
        if loop == 'WHILE':
            comp = stat[1][1]
            expr = stat[1][2]
            # TODO: infite loop limit?
            while evalCompExpr(comp): evalExpr(expr)


    # -- main
    for lineno in sorted(program.keys()):
        stat = program[lineno]
        logger.dbg("%s:" % lineno, stat)
        evalStat(stat)


    print()
    print("*******************************************************")
    print(vartypes.varsTableRepr())
    print("*******************************************************")
    print()
