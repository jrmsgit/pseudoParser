varsTable = dict()

class _base(object):
    _typ = None
    _val = None

    def __init__(self, typ):
        self._typ = typ

    def __repr__(self):
        return "<%s:%s>" % (self._typ, self._val)

    def __str__(self):
        return str(self._val)

    def setVal(self, val):
        self._val = val


class intVar(_base):
    def __init__(self):
        super(intVar, self).__init__('int')


class colaVar(_base):
    def __init__(self):
        super(colaVar, self).__init__('cola')
