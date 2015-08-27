from ..errors import *
from . import numbers, colas


def _dbg(*args):
    print('D:%s' % __name__, '-', *args)


_varsTable = dict()
reserved = numbers.reserved + colas.reserved
classmap = numbers.classmap
classmap.update(colas.classmap)


def _getVarClass(typ):
    klass = classmap.get(typ, None)
    if klass is None:
        raise ppVarInvalidType(__name__, p[1])
    return klass


def _varDeclared(ID):
    return ID in _varsTable.keys()


def declare(p):
    "type_specifier ID"
    global _varsTable
    _dbg('declare:', p[1], p[2])
    klass = _getVarClass(p[1])
    if _varDeclared(p[2]):
        raise ppVarDeclareDone(__name__, p[2])
    _varsTable[p[2]] = klass(p[2])


def assign(p):
    "ID EQUAL expression"
    global _varsTable
    _dbg('assign:', p[1], p[2], p[3])
    if _varDeclared(p[1]):
        _varsTable[p[1]].setVal(p[3])
    else:
        raise ppVarNotDeclared(__name__, p[1])


def iniciar(p):
    "INICIAR LPAREN ID RPAREN"
    global _varsTable
    if not _varDeclared(p[3]):
        raise ppVarNotDeclared(__name__, p[3])
    v = _varsTable.get(p[3])
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
