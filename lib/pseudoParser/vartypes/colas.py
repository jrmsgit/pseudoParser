from .base import baseVar

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

class _colaVar(baseVar):

    def __init__(self, ID):
        super(_colaVar, self).__init__('cola', ID)

    def doInit(self):
        _dbg('cola initialize')
        self.setVal(list())

    def assignValidate(self, val):
        if type(val) != type(list()):
            raise TypeError(str(type(val)))
        else:
            return val

    def acolar(self, val):
        self._val.append(val)

classmap = {'cola': _colaVar}
reserved = tuple([k.upper() for k in classmap.keys()])
