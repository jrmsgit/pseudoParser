from .vartypes import *
from .lexer import tokens, lexer

varsTable = dict()

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def p_program(p):
    """program : program statement
               | statement"""
    _dbg('p_program:', p.lexer.lineno)

def p_statement_declare(p):
    "statement : type_specifier VARNAME DELIM"
    _dbg('p_statement_declare:', p.lexer.lineno)

def p_statement_assign(p):
    "statement : VARNAME EQUAL constant DELIM"
    _dbg('p_statement_assign')

def p_type_specifier(p):
    "type_specifier : INT"
    _dbg('p_type_specifier')

def p_constant(p):
    "constant : ICONST"
    _dbg('p_constant')

def p_error(p):
    _dbg('p_error')
    if p is None:
        print("EOF")
    else:
        print("%s: syntax error '%s', at line '%d'" % (__name__, p.value, p.lexer.lineno))

_dbg('build yacc parser')
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
