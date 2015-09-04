from ..logger import ppLogger
from ..vartypes.base import baseVar

logger = ppLogger(__name__)

def _acolar(args):
    logger.dbg('cmd acolar:', args)
    if isinstance(args[1], baseVar):
        args[0].acolar(args[1].getVal())
    else:
        args[0].acolar(args[1])

def _desacolar(args):
    logger.dbg('cmd desacolar:', args)
    args[0].desacolar()

def _primero(args):
    logger.dbg('cmd primero:', args)
    p = args[0].primero()
    if isinstance(p, baseVar):
        return p.getVal()
    else:
        return p

def _empty(args):
    logger.dbg('cmd empty:', args)
    return args[0].colaVacia()

cmdmap = {
    'acolar': _acolar,
    'desacolar': _desacolar,
    'primero': _primero,
    'colavacia': _empty,
}
