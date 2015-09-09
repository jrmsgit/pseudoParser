import sys
from .. import wapp


@wapp.get('/static/<filename:path>')
def staticFile(filename):
    wapp.Start()
    return wapp.StaticFile(filename)


@wapp.get('/session/')
def session():
    wapp.Start(template='session.html')
    return wapp.Render()


@wapp.post('/')
def indexPost():
    wapp.Start()
    ppCode = wapp.Req.forms.get('ppCode', '')
    wapp.Log.dbg("ppCode:", ppCode)
    if ppCode == '':
        wapp.Msg.error('el archivo está vacio')
    else:
        if wapp.Req.POST.wappCmd == 'guardar':
            return wapp.CodeSave(ppCode)
    return wapp.Render()


@wapp.get('/')
def index():
    wapp.Start()
    return wapp.Render()
