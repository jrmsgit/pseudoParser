tokens = (
    'NAME',
    'NUMBER',
    'COMMENT1',
    'COMMENT2',
)

# Tokens
literals = ['=', '+', '-', '*', '/', '(', ')', ';']

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore_COMMENT1 = r'\/\* .* \*\/'
t_ignore_COMMENT2 = r'\#.*'

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
    #~ t.lexer.skip(1)
    raise Exception("%s: invalid character '%s', at line '%d' column '%d'" % (__name__, t.value[0], t.lexer.lineno, t.lexer.lexpos))

# Build the lexer
import ply.lex as lex
lexer = lex.lex(debug=1)
