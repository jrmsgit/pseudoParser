import sys

class ppLogger(object):
    _caller = None

    def __init__(self, caller):
        self._caller = caller

    def dbg(self, *args):
        print('D:%s' % self._caller, '-', *args, file=sys.stderr)
