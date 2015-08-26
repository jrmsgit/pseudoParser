def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

reserved = (
    'INT',
)

tokens = reserved + (
    'DELIM',
    'VARNAME',
    'ICONST',
    'EQUAL',
    'NEWLINE',
)

t_ignore = ' \t\x0c'

t_DELIM = r';'
t_ICONST = r'\d+'
t_EQUAL = r'='

reserved_map = dict()
for r in reserved:
    reserved_map[r.lower()] = r

def t_VARNAME(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"VARNAME")
    return t

def t_NEWLINE(t):
    r'\n+'
    _dbg('t_NEWLINE')
    t.lexer.lineno += len(t.value)

def t_error(t):
    _dbg('t_error')
    print("%s: invalid character '%s', at line '%d' column '%d'" % (__name__, t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)

_dbg('build lexer')
import ply.lex as lex
lexer = lex.lex(debug=1)

if __name__ == '__main__':
    lex.runmain()
