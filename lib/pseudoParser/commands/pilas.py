from ..logger import ppLogger

logger = ppLogger(__name__)

def _apilar(args):
    logger.dbg('cmd apilar:', args)
    v = args[0]
    v.apilar(args[1])

def _desapilar(args):
    logger.dbg('cmd desapilar:', args[0])
    args[0].desapilar()

def _tope(args):
    logger.dbg('cmd tope:', args[0])
    return args[0].tope()

cmdmap = {
    'apilar': _apilar,
    'desapilar': _desapilar,
    'tope': _tope,
}
