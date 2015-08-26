from . import vartypes
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
    vartypes.declare(p)

# -- init_statement

def p_init_statement_1(p):
    "init_statement : assign_statement"
    pass

def p_init_statement_2(p):
    "init_statement : INICIAR LPAREN type_specifier RPAREN"
    # FIXME
    p[0] = p[3]

# -- assign_statement

def p_assign_statement_1(p):
    "assign_statement : VARNAME EQUAL constant"
    vartypes.assign(p)

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
