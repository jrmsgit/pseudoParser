from ..errors import *
from . import numbers, colas, pilas
from ..logger import ppLogger

logger = ppLogger(__name__)

_varsTable = dict()
reserved = numbers.reserved + colas.reserved + pilas.reserved

classmap = numbers.classmap
classmap.update(colas.classmap)
classmap.update(pilas.classmap)


def _getVarClass(typ):
    klass = classmap.get(typ, None)
    if klass is None:
        raise ppVarInvalidType(__name__, typ)
    return klass


def _varDeclared(ID):
    return ID in _varsTable.keys()


def progStart():
    global _varsTable
    _varsTable = dict()


def declare(typ, ID):
    "type_specifier ID"
    global _varsTable
    logger.dbg('declare:', typ, ID)
    klass = _getVarClass(typ)
    if _varDeclared(ID):
        raise ppVarDeclareDone(__name__, ID)
    _varsTable[ID] = klass(ID)


def assign(ID, expr):
    "ID expression"
    global _varsTable
    logger.dbg('assign:', ID, expr)
    if _varDeclared(ID):
        _varsTable[ID].setVal(expr)
    else:
        raise ppVarNotDeclared(__name__, ID)


def iniciar(ID):
    "INICIAR LPAREN ID RPAREN"
    global _varsTable
    if not _varDeclared(ID):
        raise ppVarNotDeclared(__name__, ID)
    v = _varsTable.get(ID)
    v.initialize()


def varsTableRepr():
    global _varsTable
    return repr(_varsTable)


def getVar(ID):
    global _varsTable
    v = _varsTable.get(ID, None)
    if v is None:
        raise ppVarNotDeclared(__name__, ID)
    return v

def isDeclared(ID):
    return _varDeclared(ID)
