import sys
import time
import os.path
import hashlib

from bottle import Bottle, template, static_file, request, response

_DEBUG = True
_CODEDIR = os.path.dirname(__file__)
_SECRET = 'SUPERSECRETPASSPHRASE'
_COOKIE_TTL = 3600 * 24 * 7
_TIME_FMT = '%d %b %Y %H:%M:%S %Z'


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


class wappSession(object):
    ID = None
    since = None
    until = None

    def __init__(self, cookie):
        self.ID = cookie['sess']
        self.since = cookie['since']
        self.until = cookie['until']
        self._initFS()

    def sinceTime(self):
        return time.strftime(_TIME_FMT, time.localtime(self.since))

    def untilTime(self):
        return time.strftime(_TIME_FMT, time.localtime(self.until))

    def _initFS(self):
        # FIXME!!
        pass


class ppWebApp(Bottle):
    _tmpl = None
    Req = None
    Log = None
    Msg = None
    Resp = None
    Sess = None

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
        self._setTemplate(template)
        cookie = self._loadCookie()
        self._loadSess(cookie)

    def _loadCookie(self):
        cn = hashlib.md5(str(_SECRET+'ppweb').encode()).hexdigest()
        self.Log.dbg('cookie name:', cn)
        c = self.Req.get_cookie(cn, secret=_SECRET)
        self.Log.dbg('cookie:', c)
        if c:
            return c
        else:
            tinit = time.time()
            cd = {
                'since': tinit,
                'sess': hashlib.md5(str(time.time()).encode()).hexdigest(),
                'until': tinit + _COOKIE_TTL,
            }
            self.Resp.set_cookie(cn, cd, secret=_SECRET, max_age=_COOKIE_TTL)
            self.Log.dbg('cookie set:', cd)
            return cd

    def _loadSess(self, cookie):
        self.Log.dbg('Session')
        self.Sess = wappSession(cookie)

    def Render(self, tmplData=None):
        self.Log.dbg('Render')
        tmplArgs = {
            'wappMessages': self.Msg.getAll(),
            'wappSession': self.Sess,
            'wappCurTime': time.strftime(_TIME_FMT, time.localtime()),
        }
        if tmplData is None: tmplData = dict()
        tmplArgs.update(tmplData)
        return template("% include('{}')".format(self._tmpl), **tmplArgs)

    def SendFile(self, filename):
        self.Log.dbg('SendFile')
        return static_file(filename, root=os.path.join(_CODEDIR, 'static'))


# create wapp
wapp = ppWebApp()

# load views / routes
from .views.index import *
