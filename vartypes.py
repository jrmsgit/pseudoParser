def _dbg(*args):
    print('D:%s' % __name__, '-', *args)

_varsTable = dict()

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


class _intVar(_base):
    def __init__(self):
        super(_intVar, self).__init__('int')


class _colaVar(_base):
    def __init__(self):
        super(_colaVar, self).__init__('cola')


_classmap = {
    'int': _intVar,
    'cola': _colaVar,
}


def _getVarClass(typ):
    klass = _classmap.get(typ, None)
    if klass is None:
        raise RuntimeError("%s: unknown type '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))
    return klass


def declare(p):
    global _varsTable
    klass = _getVarClass(p[1])
    if p[2] in _varsTable.keys():
        raise RuntimeError("%s: variable already declared '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))
    _varsTable[p[2]] = klass()


def assign(p):
    global _varsTable
    if p[1] in _varsTable.keys():
        _varsTable[p[1]].setVal(p[3])
    else:
        _dbg('undefined variable', p, dir(p))
        raise RuntimeError("%s: undefined variable '%s', line '%d', col '%d'" % (__name__, p[1], p.lexer.lineno, p.lexpos(1)))


def iniciar(p):
    global _varsTable
    _dbg('iniciar')
    pass


def varsTableRepr():
    global _varsTable
    return repr(_varsTable)
