from ..errors import *

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

class baseVar(object):
    _typ = None
    _val = None
    _ID = None

    def __init__(self, typ, ID):
        self._typ = typ
        self._ID = ID

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return "<(%s)%s:%s>" % (self._typ, self._ID, self._val)

    def getType(self):
        return self._typ

    def assignValidate(self, val):
        # should be re-implemented!
        # if not valid: raise an exception
        _dbg(self._typ, 'assignValidate NOT RE-IMPLEMENTED')
        return val

    def getVal(self):
        if self._val is None: raise ppVarNotInit(__name__, self._ID)
        else: return self._val

    def setVal(self, val):
        _dbg(self._typ, 'setVal', self._ID, str(val))
        try:
            self._val = self.assignValidate(val)
        except Exception as e:
            _dbg(e)
            raise ppVarInvalidAssign(__name__, self._ID, self._typ, val)

    def initialize(self):
        if self._val is not None:
            raise ppVarInitDone(__name__, self._ID)
        self.doInit()

    def doInit(self):
        # should be re-implemented!
        _dbg(self._typ, 'doInit NOT RE-IMPLEMENTED')
