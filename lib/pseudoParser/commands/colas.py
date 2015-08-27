def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def _acolar(args):
    _dbg('cmd acolar:', args)
    v = args[0]
    if v.getType() == 'cola':
        v.acolar(args[1])

def _desacolar(args):
    _dbg('cmd desacolar:', args)

cmdmap = {
    'acolar': _acolar,
    'desacolar': _desacolar,
}
