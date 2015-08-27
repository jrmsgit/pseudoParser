from .base import baseVar

def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

class _intVar(baseVar):

    def __init__(self, ID):
        super(_intVar, self).__init__('int', ID)

    def doInit(self):
        pass

    def assignValidate(self, val):
        _dbg(self._typ, 'assing validate', self._ID)
        return int(val)

classmap = {'int': _intVar}
reserved = tuple([k.upper() for k in classmap.keys()])
