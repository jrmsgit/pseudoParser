from . import errors

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

reserved = (
    # -- type_specifier
    'INT',
    'COLA',

    # -- init_func
    'INICIAR',
)

tokens = reserved + (
    'DELIM',
    'ID',
    'ICONST',
    'EQUAL',
    'LPAREN',
    'RPAREN',
)

t_ignore = ' \t\x0c'
t_ICONST = r'\d+'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

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
    t.lexer.lineno += len(t.value)

def t_error(t):
    _dbg('t_error')
    raise errors.ppInvalidToken(__name__, t.value[0])

_dbg('build lexer')
import ply.lex as lex
lexer = lex.lex(debug=1)

# attach lexer to errors module
errors.lexer = lexer

if __name__ == '__main__':
    lex.runmain()
