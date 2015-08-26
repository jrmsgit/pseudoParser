varsTable = dict()

class _base(object):
    _typ = None
    _val = None

    def __init__(self, typ):
        self._typ = typ

    def __str__(self):
        return "<%s:%s>" % (self._typ, self._val)

    def __repr__(self):
        return self.__str__()

    def setVal(self, val):
        self._val = val

class intVar(_base):
    def __init__(self):
        super(intVar, self).__init__('int')
