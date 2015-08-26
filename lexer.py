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
    'VARNAME',
    'ICONST',
    'EQUAL',
    'LPAREN',
    'RPAREN',
)

t_ignore = ' \t\x0c'

t_DELIM = r';'
t_ICONST = r'\d+'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

reserved_map = dict()
for r in reserved:
    reserved_map[r.lower()] = r

_dbg('reserved_map:', reserved_map)

def t_VARNAME(t):
    r'[A-Za-z_][\w_]*'
    _dbg('VARNAME:', t.value)
    t.type = reserved_map.get(t.value,"VARNAME")
    _dbg('VARTYPE:', t.type)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    _dbg('t_NEWLINE:', t.lexer.lineno)

def t_error(t):
    _dbg('t_error')
    print("%s: invalid character '%s', at line '%d' column '%d'" % (__name__, t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)

_dbg('build lexer')
import ply.lex as lex
lexer = lex.lex(debug=1)

if __name__ == '__main__':
    lex.runmain()
