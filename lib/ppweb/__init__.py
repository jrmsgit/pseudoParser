import os.path
from bottle import Bottle, template, static_file

_DEBUG = True
_CODEDIR = os.path.dirname(__file__)


class ppWebApp(Bottle):
    _tmpl = None

    def __init__(self):
        self.template('index.html')
        return super(ppWebApp, self).__init__()

    def template(self, tname):
        self._tmpl = os.path.join('ppweb', 'templates', tname)

    def run(self):
        return super(ppWebApp, self).run(host='jrmsdev.local', debug=_DEBUG)

    def render(self):
        return template("% include('{}')".format(self._tmpl))

    def send_file(self, filename):
        return static_file(filename, root=os.path.join(_CODEDIR, 'static'))


wapp = ppWebApp()

# load views / routes
from .views.index import *
