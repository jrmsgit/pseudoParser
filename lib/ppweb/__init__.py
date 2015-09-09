import sys
import time
import os.path
from bottle import Bottle, template, static_file, request, response

_DEBUG = True
_CODEDIR = os.path.dirname(__file__)


class wappLogger(object):
    def log(self, *args):
        print(*args, file=sys.stderr)

    def dbg(self, *args):
        self.log('DEBUG -', *args)


class wappMessages(object):
    _msgs = None

    def __init__(self):
        self._msgs = dict()

    def error(self, msg):
        self._msgs[time.time()] = ('ERROR', msg)

    def getAll(self):
        m = list()
        for mk in sorted(self._msgs.keys()):
            m.append(self._msgs[mk])
        self._msgs = dict()
        return m


class ppWebApp(Bottle):
    _tmpl = None
    Req = None
    Log = None
    Msg = None
    Resp = None

    def __init__(self):
        self.Log = wappLogger()
        self.Log.dbg('init')
        self.Req = request
        self.Msg = wappMessages()
        self.Resp = response
        return super(ppWebApp, self).__init__()

    def _setTemplate(self, tname):
        self._tmpl = os.path.join('ppweb', 'templates', tname)

    def Run(self):
        self.Log.dbg('Run')
        return super(ppWebApp, self).run(host='jrmsdev.local', debug=_DEBUG)

    def Start(self, template='index.html'):
        self.Log.dbg('Start')

        # template
        self._setTemplate(template)

        # ppweb cookie
        self.Log.dbg('cookies:', self.Req.cookies.keys())
        cookie = self.Req.get_cookie('ppweb')
        self.Log.dbg('ppweb cookie:', cookie)
        if not cookie:
            self.Resp.set_cookie('ppweb', 'LALALA')

    def Render(self):
        self.Log.dbg('Render')
        tmplArgs = {
            'wappMessages': self.Msg.getAll(),
        }
        return template("% include('{}')".format(self._tmpl), **tmplArgs)

    def SendFile(self, filename):
        self.Log.dbg('SendFile')
        return static_file(filename, root=os.path.join(_CODEDIR, 'static'))


# create wapp
wapp = ppWebApp()

# load views / routes
from .views.index import *
