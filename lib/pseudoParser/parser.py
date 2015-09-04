from . import errors, commands
from .vartypes import numbers, colas, pilas
from .logger import ppLogger

logger = ppLogger(__name__)

keywords = (
    'IF',
    'WHILE',
    'INICIALIZAR',
)
reserved = keywords + commands.reserved + numbers.reserved
reserved += colas.reserved + pilas.reserved

tokens = reserved + (
    'DELIM',
    'ID',
    'ICONST',
    'EQUAL',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'EQ',
    'NE',
    'GT',
    'GE',
    'LT',
    'LE',
    'LBRACE',
    'RBRACE',
)

t_ignore = ' \t\x0c'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_LBRACE = r'\{'
t_RBRACE = r'\}'

reserved_map = dict()
for r in reserved:
    reserved_map[r.lower()] = r

logger.dbg('reserved_map:', reserved_map)

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    logger.dbg('ID:', t.value)
    t.type = reserved_map.get(t.value,"ID")
    logger.dbg('IDTYPE:', t.type)
    return t

def t_DELIM(t):
    r';'
    logger.dbg('DELIM: line ', t.lexer.lineno)
    return t

def t_NEWLINE(t):
    r'\n+'
    logger.dbg('NEWLINE: line ', t.lexer.lineno)
    t.lexer.lineno += t.value.count('\n')
    # ignored

def t_ICONST(t):
    r'\d+'
    logger.dbg('ICONST:', t.value)
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    logger.dbg('COMMENT: line ', t.lexer.lineno)
    t.lexer.lineno += t.value.count('\n')
    # ignored

def t_CPPCOMMENT(t):
    r'//.*\n'
    logger.dbg('CPPCOMMENT: line ', t.lexer.lineno)
    t.lexer.lineno += t.value.count('\n')
    # ignored

def t_error(t):
    logger.dbg('t_error')
    raise errors.ppInvalidToken(__name__, t.value[0])

logger.dbg('build lexer')
import ply.lex as lex

lexer = lex.lex(debug=1)
lexer.lineno = 1

# attach lexer to errors module
errors.lexer = lexer

if __name__ == '__main__':
    lex.runmain()
