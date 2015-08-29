from .base import baseVar
from ..logger import ppLogger

logger = ppLogger(__name__)

class _intVar(baseVar):

    def __init__(self, ID):
        super(_intVar, self).__init__('int', ID)

    def doInit(self):
        pass

    def assignValidate(self, val):
        logger.dbg(self._typ, 'assing validate', self._ID)
        return int(val)

classmap = {'int': _intVar}
reserved = tuple([k.upper() for k in classmap.keys()])
