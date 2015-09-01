from ..logger import ppLogger

logger = ppLogger(__name__)

def _acolar(args):
    logger.dbg('cmd acolar:', args)
    args[0].acolar(args[1])

def _desacolar(args):
    logger.dbg('cmd desacolar:', args)
    args[0].desacolar()

def _primero(args):
    logger.dbg('cmd primero:', args)
    return args[0].primero()

def _empty(args):
    logger.dbg('cmd empty:', args)
    return args[0].colaVacia()

cmdmap = {
    'acolar': _acolar,
    'desacolar': _desacolar,
    'primero': _primero,
    'colavacia': _empty,
}
