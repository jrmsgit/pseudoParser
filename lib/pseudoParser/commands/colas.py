def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def _acolar(args):
    _dbg('cmd acolar:', args)
    v = args[0]
    if v.getType() == 'cola':
        v.acolar(args[1])

def _desacolar(dst):
    _dbg('cmd desacolar:', dst)
    if dst.getType() == 'cola':
        dst.desacolar()

def _primero(dst):
    _dbg('cmd primero:', dst)
    if dst.getType() == 'cola':
        return dst.primero()

cmdmap = {
    'acolar': _acolar,
    'desacolar': _desacolar,
    'primero': _primero,
}
