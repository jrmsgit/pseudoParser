lexer = None

class ppError(Exception):
    _caller = None
    _msg = None

    def __init__(self, caller, msg):
        self._caller = caller
        self._msg = msg

    def __repr__(self):
        return "%s: %s, line '%d'" % (self._caller, self._msg, lexer.lineno)

    def __str__(self):
        return repr(self)


class ppInvalidToken(ppError):
    def __init__(self, caller, ID):
        super(ppInvalidToken, self).__init__(caller, "invalid token at '%s'" % ID)


class ppSyntaxError(ppError):
    def __init__(self, caller, p=None):
        errmsg = ''
        if p is None:
            errmsg = "unkown syntax error"
        else:
            errmsg = "syntax error at '%s'" % p.value
        super(ppSyntaxError, self).__init__(caller, errmsg)


class ppVarDeclareDone(ppError):
    def __init__(self, caller, ID):
        super(ppVarDeclareDone, self).__init__(caller, "var already declared at '%s'" % ID)


class ppVarNotDeclared(ppError):
    def __init__(self, caller, ID):
        super(ppVarNotDeclared, self).__init__(caller, "var not declared at '%s'" % ID)


class ppVarNotInit(ppError):
    def __init__(self, caller, ID):
        super(ppVarNotInit, self).__init__(caller, "var not initialized at '%s'" % ID)


class ppVarInitDone(ppError):
    def __init__(self, caller, ID):
        super(ppVarInitDone, self).__init__(caller, "var already initialized at '%s'" % ID)


class ppVarInvalidType(ppError):
    def __init__(self, caller, typ):
        super(ppVarInvalidType, self).__init__(caller, "invalid vartype at '%s'" % typ)


class ppVarInvalidAssign(ppError):
    def __init__(self, caller, ID, typ, val):
        super(ppVarInvalidAssign, self).__init__(caller, "invalid assign at '%s' (%s) '%s' " % (ID, typ, str(val)))
