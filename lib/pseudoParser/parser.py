from . import vartypes
from .lexer import *
from .errors import *

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

# -- program

def p_program(p):
    """program : program statement DELIM
               | statement DELIM"""
    _dbg('program ****************')

# -- statement

def p_statement(p):
    """statement : declare_statement
                 | assign_statement
                 | init_statement"""
    _dbg('statement')

# -- declare_statement

def p_declare_statement(p):
    "declare_statement : type_specifier ID"
    _dbg('declare_statement')
    vartypes.declare(p)

# -- init_statement

def p_init_statement(p):
    "init_statement : INICIAR LPAREN ID RPAREN"
    _dbg('init_statement')
    vartypes.iniciar(p)

# -- assign_statement

def p_assign_statement(p):
    "assign_statement : ID EQUAL expression"
    _dbg('assign_statement', len(p))
    vartypes.assign(p)

# -- type_specifier

def p_type_specifier(p):
    """type_specifier : INT
                      | COLA"""
    _dbg('type_specifier')
    p[0] = p[1]

# -- expression

def p_expression(p):
    "expression : constant"
    _dbg('expression <', ' '.join(p[1:]), '>')
    p[0] = p[1]

# -- constant

def p_constant(p):
    "constant : ICONST"
    _dbg("constant <%s>" % p[1])
    p[0] = p[1]

# -- error

def p_error(p):
    _dbg('p_error')
    if p is None:
        _dbg('lexer skip token (empty line or EOF?), line', lexer.lineno - 1)
        lexer.skip(1)
    else:
        raise ppSyntaxError(__name__, p)

# -- build the parser

_dbg('build yacc parser')
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
