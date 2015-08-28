from . import errors, commands
from .vartypes import numbers, colas, pilas

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

reserved = (
    # -- init_func
    'INICIAR',
) + commands.reserved + numbers.reserved
reserved += colas.reserved + pilas.reserved

tokens = reserved + (
    'DELIM',
    'ID',
    'ICONST',
    'EQUAL',
    'LPAREN',
    'RPAREN',
    'COMMA',
)

t_ignore = ' \t\x0c'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

reserved_map = dict()
for r in reserved:
    reserved_map[r.lower()] = r

_dbg('reserved_map:', reserved_map)

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    _dbg('ID:', t.value)
    t.type = reserved_map.get(t.value,"ID")
    _dbg('IDTYPE:', t.type)
    return t

def t_DELIM(t):
    r';'
    _dbg('DELIM: line ', t.lexer.lineno)
    return t

def t_NEWLINE(t):
    r'\n+'
    _dbg('NEWLINE: line ', t.lexer.lineno)
    t.lexer.lineno += t.value.count('\n')

def t_ICONST(t):
    r'\d+'
    _dbg('ICONST:', t.value)
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    _dbg('COMMENT: line ', t.lexer.lineno)
    t.lexer.lineno += t.value.count('\n')

def t_CPPCOMMENT(t):
    r'//.*\n'
    _dbg('CPPCOMMENT: line ', t.lexer.lineno)
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    _dbg('t_error')
    raise errors.ppInvalidToken(__name__, t.value[0])

_dbg('build lexer')
import ply.lex as lex

lexer = lex.lex(debug=1)
lexer.lineno = 1

# attach lexer to errors module
errors.lexer = lexer

if __name__ == '__main__':
    lex.runmain()
