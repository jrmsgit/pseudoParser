from . import colas

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def _print(args):
    _dbg('cmd print:', args)
    if isinstance(args, tuple):
        for i in list(args): print(i, end=' ')
        print()
    else:
        print(args)

_cmdmap = {
    'print': _print,
}
_cmdmap.update(colas.cmdmap)

_rk = list()
for k in _cmdmap.keys():
    _rk.append(k.upper())
reserved = tuple(_rk)

def run(cmd, args):
    _dbg('run', cmd, args)
    f = _cmdmap.get(cmd, None)
    return f(args)
