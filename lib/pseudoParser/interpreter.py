from . import vartypes, commands
from .logger import ppLogger

logger = ppLogger(__name__)

def runprog(program):

    def cmdStat(stat):
        logger.dbg('cmdStat:', stat)
        args = list()
        for a in stat[2]:
            args.append(evalExpr(a))
        return commands.run(stat[1], args)

    def evalStat(stat):
        logger.dbg('evalStat:', stat)
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
        if isinstance(expr, dict):
            logger.dbg('dict expr:', expr)
            for ek in sorted(expr.keys()):
                evalStat(expr[ek])

        elif vartypes.isDeclared(expr):
            # ID expression
            logger.dbg('ID expr:', expr)
            return vartypes.getVar(expr).getVal()

        else:
            # constant expression
            logger.dbg('constant expr:', expr)
            return expr

    def evalCompExpr(expr):
        logger.dbg('evalCompExpr:', expr[0], expr[1], expr[2])
        v = None
        if expr[1] == '==': v =  evalExpr(expr[0]) == evalExpr(expr[2])
        if expr[1] == '!=': v =  evalExpr(expr[0]) != evalExpr(expr[2])
        if expr[1] == '>': v =  evalExpr(expr[0]) > evalExpr(expr[2])
        if expr[1] == '>=': v =  evalExpr(expr[0]) >= evalExpr(expr[2])
        if expr[1] == '<': v =  evalExpr(expr[0]) < evalExpr(expr[2])
        if expr[1] == '<=': v =  evalExpr(expr[0]) <= evalExpr(expr[2])
        logger.dbg('comp was:', v)
        return v

    def condStat(stat):
        logger.dbg('condStat:', stat[1][0], stat[1][1], stat[1][2])
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
    for statnr in sorted(program.keys()):
        stat = program[statnr]
        logger.dbg("%d:" % statnr, stat)
        evalStat(stat)


    logger.dbg()
    logger.dbg("*******************************************************")
    logger.dbg(vartypes.varsTableRepr())
    logger.dbg("*******************************************************")
    logger.dbg()

# -- main
if __name__ == '__main__':
    import sys
    from .compiler import parser

    code = None
    try:
        fh = open(sys.argv[1], 'r')
        code = fh.read()
        fh.close()
    except IndexError:
        code = sys.stdin.read()

    program = parser.parse(code)
    runprog(program)
