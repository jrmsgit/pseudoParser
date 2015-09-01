import sys
from . import colas, pilas
from ..logger import ppLogger

logger = ppLogger(__name__)

def _println(args):
    logger.dbg('cmd println:', args)
    print(*args)

def _input(args):
    logger.dbg('cmd input')
    args[0].setVal(sys.stdin.readline().strip())

_cmdmap = {
    'mostrar': _println,
    'ingresar': _input,
}
_cmdmap.update(colas.cmdmap)
_cmdmap.update(pilas.cmdmap)

_rk = list()
for k in _cmdmap.keys():
    _rk.append(k.upper())
reserved = tuple(_rk)

def run(cmd, args):
    logger.dbg('run', cmd, args)
    f = _cmdmap.get(cmd, None)
    return f(args)
