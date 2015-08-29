from .base import baseVar
from ..errors import *
from ..logger import ppLogger

logger = ppLogger(__name__)

class _colaVar(baseVar):

    def __init__(self, ID):
        super(_colaVar, self).__init__('cola', ID)

    def doInit(self):
        logger.dbg('cola initialize')
        self.setVal(list())

    def assignValidate(self, val):
        if type(val) != type(list()):
            raise TypeError(str(type(val)))
        else:
            return val

    def acolar(self, val):
        if self._val is None:
            raise ppVarNotInit(__name__, self._ID)
        self._val.append(val)

    def desacolar(self):
        if self._val is None:
            raise ppVarNotInit(__name__, self._ID)
        self._val.pop(0)

    def primero(self):
        if self._val is None:
            raise ppVarNotInit(__name__, self._ID)
        r = self._val[0]
        logger.dbg('primero:', r)
        return r

classmap = {'cola': _colaVar}
reserved = tuple([k.upper() for k in classmap.keys()])
