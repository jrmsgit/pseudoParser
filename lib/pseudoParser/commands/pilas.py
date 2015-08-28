def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

def _apilar(args):
    _dbg('cmd apilar:', args)
    v = args[0]
    v.apilar(args[1])

def _desapilar(args):
    _dbg('cmd desapilar:', args[0])
    args[0].desapilar()

def _tope(args):
    _dbg('cmd tope:', args[0])
    return args[0].tope()

cmdmap = {
    'apilar': _apilar,
    'desapilar': _desapilar,
    'tope': _tope,
}
