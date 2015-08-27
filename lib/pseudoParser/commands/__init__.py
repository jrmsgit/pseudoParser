from . import colas

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

_cmdmap = colas.cmdmap

_rk = list()
for k in _cmdmap.keys():
    _rk.append(k.upper())
reserved = tuple(_rk)

def run(cmd, args):
    _dbg('run', cmd, args)
    f = _cmdmap.get(cmd, None)
    return f(args)
