#!/usr/bin/python3
# Stolen from: http://www.dabeaz.com/ply/example.html

tokens = (
    'NAME',
    'NUMBER',
)

# Tokens
literals = ['=', '+', '-', '*', '/', '(', ')', ';']
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex(debug=1)

# Parsing rules

precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
)

# dictionary of names
namesTable = dict()

def p_statement_assign(p):
    "statement : NAME '=' expression ';'"
    namesTable[p[1]] = p[3]

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
        p[0] = namesTable[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p is None:
        print("End of file!!")
    else:
        print("Syntax error at '%s', line '%d'" % (p.value, lex.lexer.lineno))

import ply.yacc as yacc
parser = yacc.yacc(debug=1)

import sys
try:
    fh = open(sys.argv[1], 'r')
    parser.parse(fh.read())
    fh.close()
except IndexError:
    parser.parse(sys.stdin.read())

print()
print("*******************************************************")
print()
print(namesTable)
