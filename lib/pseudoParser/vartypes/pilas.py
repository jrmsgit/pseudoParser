from .base import baseVar
from ..errors import *

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

class _pilaVar(baseVar):

    def __init__(self, ID):
        super(_pilaVar, self).__init__('pila', ID)

    def doInit(self):
        _dbg('pila initialize')
        self.setVal(list())

    def assignValidate(self, val):
        if type(val) != type(list()):
            raise TypeError(str(type(val)))
        else:
            return val

    def apilar(self, val):
        if self._val is None:
            raise ppVarNotInit(__name__, self._ID)
        self._val.append(val)

    def desapilar(self):
        if self._val is None:
            raise ppVarNotInit(__name__, self._ID)
        self._val.pop()

    def tope(self):
        if self._val is None:
            raise ppVarNotInit(__name__, self._ID)
        r = self._val[-1]
        _dbg('tope:', r)
        return r

classmap = {'pila': _pilaVar}
reserved = tuple([k.upper() for k in classmap.keys()])
