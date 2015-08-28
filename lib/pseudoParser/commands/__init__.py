from . import colas

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def _println(args):
    _dbg('cmd println:', args)
    print(*args)

_cmdmap = {
    'println': _println,
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
