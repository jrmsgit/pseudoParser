import os
import sys
import time
import os.path
import hashlib

from bottle import Bottle, template, static_file, request, response, redirect

_VERSION = 150909
_DEBUG = True
_CODEDIR = os.path.dirname(__file__)
_SECRET = 'SUPERSECRETPASSPHRASE'
_COOKIE_TTL = 3600 * 24 * 7
_TIME_FMT = '%d %b %Y %H:%M:%S %Z'
_SESS_DIR = '/var/tmp/ppwebSessions'


class wappLogger(object):
    def log(self, *args):
        print(*args, file=sys.stderr)

    def dbg(self, *args):
        self.log('DEBUG -', *args)


class wappMessages(object):
    _msgs = None
    _sess = None

    def __init__(self, sess):
        self._msgs = dict()
        self._sess = sess

    def error(self, msg):
        self._msgs[time.time()] = ('ERROR', msg)

    def info(self, msg):
        self._msgs[time.time()] = ('INFO', msg)

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
    dirPath = None
    Log = wappLogger()

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
        self.dirPath = os.path.join(_SESS_DIR, self.ID[0], self.ID[1], self.ID)
        os.makedirs(self.dirPath, mode=0o770, exist_ok=True)
        self.Log.dbg('session dir:', self.dirPath)

    def writeFile(self, fname, content):
        fpath = os.path.join(self.dirPath, fname)
        with open(fpath, 'w') as fh:
            fh.truncate()
            fh.write(content)
            fh.close()

    def readFile(self, fname):
        fpath = os.path.join(self.dirPath, fname)
        with open(fpath, 'r') as fh:
            fh.truncate()
            content = fh.read()
            fh.close()
            return content


class ppWebApp(Bottle):
    _tmpl = None
    Req = None
    Log = None
    Msg = None
    Resp = None
    Sess = None
    _startTime = None

    def __init__(self):
        self.Log = wappLogger()
        self.Log.dbg('init')
        self.Req = request
        self.Resp = response
        return super(ppWebApp, self).__init__()

    def _setTemplate(self, tname):
        self._tmpl = os.path.join('ppweb', 'templates', tname)

    def Run(self):
        self.Log.dbg('Run')
        return super(ppWebApp, self).run(host='jrmsdev.local', debug=_DEBUG)

    def Start(self, tmpl='index.html'):
        self.Log.dbg('Start:', self.Req)
        self._startTime = time.time()
        self._setTemplate(tmpl)
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
        self.Log.dbg('Session:', cookie['sess'])
        self.Sess = wappSession(cookie)
        self.Msg = wappMessages(self.Sess)

    def Render(self, tmplData=None, tmpl=None):
        self.Log.dbg('Render')
        tmplArgs = {
            'wappVersion': _VERSION,
            'wappMessages': self.Msg.getAll(),
            'wappSession': self.Sess,
            'wappCurTime': time.strftime(_TIME_FMT, time.localtime()),
        }
        if tmpl is not None:
            self._setTemplate(tmpl)
        if tmplData is None:
            tmplData = dict()
        tmplArgs.update(tmplData)
        tmplArgs.update({'wappTook': '%.5f' % (time.time() - self._startTime)})
        return template("% include('{}')".format(self._tmpl), **tmplArgs)

    def StaticFile(self, filename):
        self.Log.dbg('StaticFile')
        return static_file(filename, root=os.path.join(_CODEDIR, 'static'))

    def CodeSave(self, code):
        self.Log.dbg('CodeSave')
        fname = 'editor.src'
        self.Sess.writeFile(fname, code)
        return static_file(fname, root=self.Sess.dirPath, download=fname)

    def Redirect(self, location):
        self.Log.dbg('Redirect')
        return redirect(location)


# create wapp
wapp = ppWebApp()

# load views / routes
from .views.index import *
