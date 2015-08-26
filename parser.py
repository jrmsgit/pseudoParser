from .vartypes import *
from .lexer import *

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

# -- program

def p_program(p):
    """program : program statement
               | statement"""
    _dbg('p_program')

# -- statement

def p_statement_1(p):
    "statement : declare_statement DELIM"
    pass

def p_statement_2(p):
    "statement : init_statement DELIM"
    pass

# -- declare_statement

def p_declare_statement(p):
    "declare_statement : type_specifier VARNAME"
    _dbg('p_declare_statement:', p)
    if p[2] in varsTable.keys():
        _dbg('var already declared')
        raise RuntimeError("%s: variable already declared '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))
    if p[1] == 'int':
        varsTable[p[2]] = intVar()
    elif p[1] == 'cola':
        varsTable[p[2]] = colaVar()
    else:
        raise RuntimeError("%s: unknown type '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))

# -- init_statement

def p_init_statement_1(p):
    "init_statement : VARNAME EQUAL constant"
    if p[1] in varsTable.keys():
        varsTable[p[1]].setVal(p[3])
    else:
        _dbg('undefined variable', p, dir(p))
        raise RuntimeError("%s: undefined variable '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))

def p_init_statement_2(p):
    "init_statement : INICIAR LPAREN type_specifier RPAREN"
    p[0] = p[3]

# -- type_specifier

def p_type_specifier(p):
    """type_specifier : INT
                      | COLA"""
    p[0] = p[1]

# -- constant

def p_constant(p):
    "constant : ICONST"
    p[0] = p[1]

# -- error

def p_error(p):
    _dbg('p_error')
    if p is None:
        raise RuntimeError("%s: unkown syntax error at line '%d'" % (__name__, lexer.lineno))
    else:
        raise RuntimeError("%s: syntax error '%s', at line '%d'" % (__name__, p.value, p.lexer.lineno))

# -- build the parser

_dbg('build yacc parser')
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
