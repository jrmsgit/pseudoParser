from .errors import *

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

_varsTable = dict()

class _base(object):
    _typ = None
    _val = None
    _ID = None

    def __init__(self, typ, ID):
        self._typ = typ
        self._ID = ID

    def __repr__(self):
        return "<(%s)%s:%s>" % (self._typ, self._ID, self._val)

    def __str__(self):
        return str(self._val)

    def assignValidate(self, val):
        # should be re-implemented!
        # if not valid: raise an exception
        _dbg(self._typ, 'assignValidate NOT RE-IMPLEMENTED')

    def setVal(self, val):
        _dbg(self._typ, 'setVal', self._ID)
        self.assignValidate(val)
        self._val = val
        _dbg(self._typ, 'val set:', val)

    def initialize(self):
        if self._val is not None:
            raise ppVarInitDone(__name__, self._ID)
        self.doInit()

    def doInit(self):
        # should be re-implemented!
        _dbg(self._typ, 'doInit NOT RE-IMPLEMENTED')


class _intVar(_base):

    def __init__(self, ID):
        super(_intVar, self).__init__('int', ID)

    def doInit(self):
        pass


class _colaVar(_base):

    def __init__(self, ID):
        super(_colaVar, self).__init__('cola', ID)

    def doInit(self):
        _dbg('cola initialize')
        self.setVal(list())


_classmap = {
    'int': _intVar,
    'cola': _colaVar,
}


def _getVarClass(typ):
    klass = _classmap.get(typ, None)
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
    _dbg('assign:', p[0], p[1], p[2], p[3])
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