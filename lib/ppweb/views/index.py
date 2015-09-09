import sys
from .. import wapp


@wapp.get('/')
def index():
    wapp.Start()
    return wapp.Render()


@wapp.get('/static/<filename:path>')
def sendFile(filename):
    wapp.Start()
    return wapp.SendFile(filename)


@wapp.post('/exec/')
def codeExec():
    wapp.Start(template='exec.html')
    ppCode = wapp.Req.forms.get('ppCode', '')
    wapp.Log.dbg("ppCode:", ppCode)
    if ppCode == '':
        wapp.Msg.error('no hay código para ejecutar')
    return wapp.Render()


@wapp.get('/session/')
def session():
    wapp.Start(template='session.html')
    return wapp.Render()
