from .vartypes import *
from .lexer import tokens

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

#~ precedence = (
    #~ ('left','+','-'),
    #~ ('left','*','/'),
    #~ ('right','UMINUS'),
#~ )

varsTable = dict()

def p_declaration(p):
    "declaration : declaration_specifier DELIM"
    _dbg('p_declaration')

def p_declaration_specifier(p):
    "declaration_specifier : type_specifier VARNAME"
    _dbg('p_declaration_specifier')

def p_type_specifier(p):
    """type_specifier : INT"""
    _dbg('p_type_specifier')

def p_error(p):
    _dbg('p_error')
    if p is None:
        print("EOF")
    else:
        print("%s: syntax error '%s', at line '%d'" % (__name__, p.value, p.lexer.lineno))

_dbg('build yacc parser')
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
