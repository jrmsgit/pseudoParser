from . import vartypes, commands, compiler
from .logger import ppLogger

logger = ppLogger(__name__)
curstat = 0
statements = None

def runprog(program):
    global curstat, statements
    statements = dict()
    vartypes.progStart()
    compiler.progStart()

    def cmdStat(stat):
        logger.dbg('cmdStat:', stat)
        args = list()
        for a in stat[2]:
            args.append(evalExpr(a))
        return commands.run(stat[1], args)

    def evalStat(snr, stat):
        logger.dbg('evalStat:', snr, stat)
        global curstat, statements
        curstat = snr

        statements[snr] = stat

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
        # statements block / program
        if isinstance(expr, dict):
            logger.dbg('dict expr:', expr)
            for ek in sorted(expr.keys()):
                evalStat(ek, expr[ek])

        # constant expression
        elif isinstance(expr, tuple) and expr[0] == 'CONSTEXPR':
            logger.dbg('constant expr:', expr)
            return expr[1]

        # command statement
        elif isinstance(expr, tuple) and expr[0] == 'COMMAND':
            return cmdStat(expr)

        # ID expression (default)
        else:
            logger.dbg('ID expr:', expr)
            return vartypes.getVar(expr).getVal()

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
        evalStat(statnr, stat)

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
    print(statements)
