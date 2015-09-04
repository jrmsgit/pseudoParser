from ..logger import ppLogger
from ..vartypes.base import baseVar

logger = ppLogger(__name__)

def _apilar(args):
    logger.dbg('cmd apilar:', args)
    v = args[0]
    if isinstance(args[1], baseVar):
        v.apilar(args[1].getVal())
    else:
        v.apilar(args[1])

def _desapilar(args):
    logger.dbg('cmd desapilar:', args[0])
    args[0].desapilar()

def _tope(args):
    logger.dbg('cmd tope:', args[0])
    t = args[0].tope()
    if isinstance(t, baseVar):
        return t.getVal()
    else:
        return t

def _empty(args):
    logger.dbg('cmd empty:', args)
    return args[0].pilaVacia()

cmdmap = {
    'apilar': _apilar,
    'desapilar': _desapilar,
    'tope': _tope,
    'pilavacia': _empty,
}
