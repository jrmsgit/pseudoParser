def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def _acolar(args):
    _dbg('cmd acolar:', args)
    v = args[0]
    v.acolar(args[1])

def _desacolar(args):
    _dbg('cmd desacolar:', args[0])
    args[0].desacolar()

def _primero(args):
    _dbg('cmd primero:', args[0])
    return args[0].primero()

cmdmap = {
    'acolar': _acolar,
    'desacolar': _desacolar,
    'primero': _primero,
}
