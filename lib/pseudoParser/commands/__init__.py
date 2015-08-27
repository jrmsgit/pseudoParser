def _dbg(*args):
    print('D:%s' % __name__, '-', *args)


def _acolar(args):
    _dbg('cmd acolar:', args)
    v = args[0]
    if v.getType() == 'cola':
        v.acolar(args[1])


_cmdmap = {
    'acolar': _acolar,
}


_rk = list()
for k in _cmdmap.keys():
    _rk.append(k.upper())
reserved = tuple(_rk)


def run(cmd, args):
    _dbg('run', cmd, args)
    f = _cmdmap.get(cmd, None)
    f(args)
