from . import vartypes, commands, compiler, runtime
from .logger import ppLogger

logger = ppLogger(__name__)
curstat = 0
statements = None

def runprog(program):
    global curstat, statements
    statements = dict()

    vartypes.progStart()
    compiler.progStart()
    runtime.progStart()

    def cmdStat(stat):
        logger.dbg('cmdStat:', stat)
        args = list()
        for a in stat[2]:
            args.append(evalExpr(a))
        return commands.run(stat[1], args)

    def evalExpr(expr):
        # statements block / program
        if isinstance(expr, dict):
            logger.dbg('dict expr:', expr)
            for ek in sorted(expr.keys()):
                evalStat(ek, expr[ek])

        # statement
        elif isinstance(expr, tuple):
            logger.dbg('tuple expr:', expr)

            # ID
            if expr[0] == 'ID':
                return vartypes.getVar(expr[1])

            # constant
            elif expr[0] == 'CONSTANT':
                return expr[1]

            # command
            elif expr[0] == 'COMMAND':
                return cmdStat(expr)

            # comparison
            elif expr[0] == 'COMPARISON':
                return evalCompExpr(expr)

            # invalid expression
            else:
                raise RuntimeError('invalid tuple expression: %s' % str(expr))

        # invalid expression
        else:
            raise RuntimeError('invalid dict expression: %s' % str(expr))

    def evalCompExpr(expr):
        logger.dbg('evalCompExpr:', expr)
        v = None
        l = evalExpr(expr[1])
        r = evalExpr(expr[3])
        if isinstance(l, vartypes.base.baseVar): l = l.getVal()
        if isinstance(r, vartypes.base.baseVar): r = r.getVal()
        if expr[2] == '==': v = l == r
        elif expr[2] == '!=': v = l != r
        elif expr[2] == '>': v = l > r
        elif expr[2] == '>=': v = l >= r
        elif expr[2] == '<': v = l < r
        elif expr[2] == '<=': v = l <= r
        else: raise RuntimeError('invalid comparison expression: %s' % str(expr))
        logger.dbg('comparison was:', v)
        return v

    def condStat(stat):
        logger.dbg('condStat:', stat)
        cond = stat[1]
        if cond == 'IF':
            if evalExpr(stat[2]): return evalExpr(stat[3])
            else: return False
        else:
            raise RuntimeError('invalid conditional statement: %s' % str(stat))

    def loopStat(stat):
        logger.dbg('loopStat:', stat)
        loop = stat[1][0]
        if loop == 'WHILE':
            comp = stat[1][1]
            expr = stat[1][2]
            # TODO: infite loop limit?
            while evalExpr(comp): evalExpr(expr)
        else:
            raise RuntimeError('invalid loop statement: %s' % str(stat))

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

        elif stat[0] == 'CONDITIONAL':
            condStat(stat)

        elif stat[0] == 'LOOP':
            loopStat(stat)

        else:
            raise RuntimeError('invalid statement: %s' % str(stat))

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
    from . import runtime

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

    runtime.output.seek(0, 0)
    for l in runtime.output.readlines():
        print(l, end='')
