from ..logger import ppLogger

logger = ppLogger(__name__)

def _acolar(args):
    logger.dbg('cmd acolar:', args)
    v = args[0]
    v.acolar(args[1])

def _desacolar(args):
    logger.dbg('cmd desacolar:', args[0])
    args[0].desacolar()

def _primero(args):
    logger.dbg('cmd primero:', args[0])
    return args[0].primero()

cmdmap = {
    'acolar': _acolar,
    'desacolar': _desacolar,
    'primero': _primero,
}
