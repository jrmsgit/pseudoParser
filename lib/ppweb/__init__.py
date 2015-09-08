import os.path
from bottle import Bottle, template, static_file, request

_DEBUG = True
_CODEDIR = os.path.dirname(__file__)


class ppWebApp(Bottle):
    _tmpl = None
    Req = None

    def __init__(self):
        self.Req = request
        self.Template('index.html')
        return super(ppWebApp, self).__init__()

    def Template(self, tname):
        self._tmpl = os.path.join('ppweb', 'templates', tname)

    def Run(self):
        return super(ppWebApp, self).run(host='jrmsdev.local', debug=_DEBUG)

    def Render(self):
        return template("% include('{}')".format(self._tmpl))

    def SendFile(self, filename):
        return static_file(filename, root=os.path.join(_CODEDIR, 'static'))


# create wapp
wapp = ppWebApp()

# load views / routes
from .views.index import *
