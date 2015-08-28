from .parser import tokens, lexer
from .errors import ppSyntaxError

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

# -- program

def p_program(p):
    """program : program statement
               | statement"""
    _dbg('program ****************')
    if len(p) == 2 and p[1]:
        p[0] = dict()
        p[0][lexer.lineno] = p[1]
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]: p[0] = dict()
        if p[2]:
            p[0][lexer.lineno] = p[2]

# -- statement

def p_statement(p):
    """statement : declare_statement DELIM
                 | assign_statement DELIM
                 | init_statement DELIM
                 | command_statement DELIM"""
    _dbg('statement')
    if isinstance(p[1], tuple):
        p[0] = p[1]

# -- declare_statement

def p_declare_statement(p):
    "declare_statement : type_specifier ID"
    _dbg('declare_statement')
    p[0] = ('DECLARE', p[1], p[2])

# -- init_statement

def p_init_statement(p):
    "init_statement : INICIAR LPAREN ID RPAREN"
    _dbg('init_statement')
    p[0] = ('INIT', p[1], p[3])

# -- assign_statement

def p_assign_statement(p):
    "assign_statement : ID EQUAL expression"
    _dbg('assign_statement:', p[1], p[3])
    p[0] = ('ASSIGN', p[1], p[3])

# -- type_specifier

def p_type_specifier(p):
    """type_specifier : INT
                      | COLA"""
    _dbg('type_specifier')
    p[0] = p[1]

# -- expression

def p_expression_1(p):
    "expression : ID"
    _dbg('expression:', p[1])
    p[0] = p[1]

def p_expression_2(p):
    """expression : constant
                  | command_statement"""
    _dbg('expression:', p[1])
    p[0] = p[1]

# -- constant

def p_constant(p):
    "constant : ICONST"
    _dbg("constant <%s>" % p[1])
    p[0] = p[1]

# -- command_statement

def p_command_statement(p):
    "command_statement : command LPAREN command_args RPAREN"
    _dbg("command_statement:", p[1], p[3])
    p[0] = ('COMMAND', p[1], p[3])

# -- command

def p_command(p):
    """command : PRINTLN
               | ACOLAR
               | DESACOLAR
               | PRIMERO"""
    _dbg("command", p[1])
    p[0] = p[1]

# -- command_args

def p_command_args_2(p):
    "command_args : ID COMMA ID"
    _dbg('command_args:', p[1], p[3])
    p[0] = (p[1], p[3])

def p_command_args_3(p):
    "command_args : ID COMMA constant"
    _dbg('command_args:', p[1], p[3])
    p[0] = (p[1], p[3])

def p_command_args_1(p):
    "command_args : expression"
    _dbg('command_args:', p[1])
    p[0] = (p[1],)

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
