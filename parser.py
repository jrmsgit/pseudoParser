from .lexer import *

# FIXME: Esto es bastante feo...
from . import vartypes
vartypes.lex = lex
from .vartypes import *

# Parsing rules

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
)

def p_statement_expr(p):
    "statement : expression ';'"
    print(p[1])

def p_expression_binop(p):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression"""
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = varsTable[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = None

def p_error(p):
    if p is None:
        print("End of file!!")
    else:
        raise RuntimeError("%s: syntax error '%s', at line '%d'" % (__name__, p.value, lex.lexer.lineno))

# Build the parser
import ply.yacc as yacc
parser = yacc.yacc(debug=1)
