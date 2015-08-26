from .vartypes import *
from .lexer import *

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)



def p_program(p):
    """program : program statement
               | statement"""
    _dbg('p_program')



def p_statement_declare(p):
    "statement : type_specifier VARNAME DELIM"
    _dbg('p_statement_declare')
    if p[2] in varsTable.keys():
        _dbg('var already declared')
        raise RuntimeError
    else:
        varsTable[p[2]] = intVar()

def p_statement_assign(p):
    "statement : VARNAME EQUAL constant DELIM"
    if p[1] in varsTable.keys():
        varsTable[p[1]].setVal(p[3])
    else:
        _dbg('undefined variable', p, dir(p))
        raise RuntimeError("%s: undefined variable '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))



def p_type_specifier(p):
    "type_specifier : INT"
    _dbg('p_type_specifier')

def p_constant(p):
    "constant : ICONST"
    _dbg('p_constant')
    p[0] = p[1]



def p_error(p):
    _dbg('p_error')
    if p is None:
        raise RuntimeError("%s: error at line '%d'" % (__name__, lexer.lineno))
    else:
        raise RuntimeError("%s: syntax error '%s', at line '%d'" % (__name__, p.value, p.lexer.lineno))

_dbg('build yacc parser')
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
