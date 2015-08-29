from .parser import tokens, lexer
from .errors import ppSyntaxError
from .logger import ppLogger

logger = ppLogger(__name__)

# -- program

def p_program(p):
    """program : program statement
               | statement"""
    logger.dbg('program ****************')
    # lexer.lineno was already increased here so the -1 then
    lineno = lexer.lineno - 1
    if len(p) == 2 and p[1]:
        p[0] = dict()
        p[0][lineno] = p[1]
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]: p[0] = dict()
        if p[2]:
            p[0][lineno] = p[2]

# -- statement

def p_statement(p):
    """statement : declare_statement DELIM
                 | assign_statement DELIM
                 | init_statement DELIM
                 | command_statement DELIM
                 | conditional_statement
                 | loop_statement"""
    logger.dbg('statement')
    if isinstance(p[1], tuple):
        p[0] = p[1]

def p_statement_list(p):
    """statement_list : statement_list statement
                      | statement"""
    logger.dbg('statement_list')
    if len(p) == 2:
        p[0] = (p[1],)
    elif len(p) == 3:
        p[0] = p[1] + (p[2],)

# -- declare_statement

def p_declare_statement(p):
    "declare_statement : type_specifier ID"
    logger.dbg('declare_statement')
    p[0] = ('DECLARE', p[1], p[2])

# -- init_statement

def p_init_statement(p):
    "init_statement : INICIAR LPAREN ID RPAREN"
    logger.dbg('init_statement')
    p[0] = ('INIT', p[1], p[3])

# -- assign_statement

def p_assign_statement(p):
    "assign_statement : ID EQUAL expression"
    logger.dbg('assign_statement:', p[1], p[3])
    p[0] = ('ASSIGN', p[1], p[3])

# -- type_specifier

def p_type_specifier(p):
    """type_specifier : INT
                      | COLA
                      | PILA"""
    logger.dbg('type_specifier')
    p[0] = p[1]

# -- expression

def p_expression_1(p):
    "expression : ID"
    logger.dbg('expression:', p[1])
    p[0] = p[1]

def p_expression_2(p):
    """expression : constant
                  | command_statement"""
    logger.dbg('expression:', p[1])
    p[0] = p[1]

# -- constant

def p_constant(p):
    "constant : ICONST"
    logger.dbg("constant <%s>" % p[1])
    p[0] = p[1]

# -- command_statement

def p_command_statement(p):
    "command_statement : command LPAREN command_args RPAREN"
    logger.dbg("command_statement:", p[1], p[3])
    p[0] = ('COMMAND', p[1], p[3])

# -- command

def p_command(p):
    """command : PRINTLN
               | INGRESAR
               | ACOLAR
               | DESACOLAR
               | PRIMERO
               | APILAR
               | DESAPILAR
               | TOPE"""
    logger.dbg("command", p[1])
    p[0] = p[1]

# -- command_args

def p_command_args_2(p):
    "command_args : ID COMMA ID"
    logger.dbg('command_args:', p[1], p[3])
    p[0] = (p[1], p[3])

def p_command_args_3(p):
    "command_args : ID COMMA constant"
    logger.dbg('command_args:', p[1], p[3])
    p[0] = (p[1], p[3])

def p_command_args_1(p):
    "command_args : expression"
    logger.dbg('command_args:', p[1])
    p[0] = (p[1],)

# -- conditional_statement

def p_conditional_statement(p):
    "conditional_statement : IF LPAREN conditional_expression RPAREN LBRACE statement_list  RBRACE"
    logger.dbg('conditional_statement:', p[1].upper(), p[3], p[6])
    p[0] = ('CONDSTAT', (p[1].upper(), p[3], p[6]))

# -- conditional_expression

def p_conditional_expression(p):
    "conditional_expression : comparison_expression"
    logger.dbg('conditional_expression:', p[1])
    p[0] = p[1]

# -- comparison_expression

def p_comparison_expression(p):
    """comparison_expression : expression EQ expression
                             | expression NE expression
                             | expression GT expression
                             | expression GE expression
                             | expression LT expression
                             | expression LE expression"""
    logger.dbg('conditional_expression:', p[1], p[2], p[3])
    p[0] = (p[1], p[2], p[3])

# -- loop_statement

def p_loop_statement(p):
    "loop_statement : while_loop_statement"
    logger.dbg('loop_statement:', p[1])
    p[0] = ('LOOPSTAT', p[1])

def p_while_loop_statement(p):
    "while_loop_statement : WHILE LPAREN conditional_expression RPAREN LBRACE statement_list RBRACE"
    logger.dbg('while_loop_statement:', p[1].upper(), p[3], p[6])
    p[0] = (p[1].upper(), p[3], p[6])

# -- error

def p_error(p):
    logger.dbg('p_error')
    if p is None:
        logger.dbg('lexer skip token (empty line or EOF?), line', lexer.lineno - 1)
        lexer.skip(1)
    else:
        raise ppSyntaxError(__name__, p)

# -- build the parser

logger.dbg('build yacc parser')
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
