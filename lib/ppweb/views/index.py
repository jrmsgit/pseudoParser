import sys
import os.path
from .. import wapp


@wapp.get('/static/<filename:path>')
def staticFile(filename):
    wapp.Start()
    return wapp.StaticFile(filename)


@wapp.get('/session/')
def session():
    wapp.Start(tmpl='session.html')
    return wapp.Render()


@wapp.post('/upload/')
def uploadPost():
    wapp.Start(tmpl='upload.html')
    if wapp.Req.POST.wappCmd == 'abrir':
        ppcode = wapp.Req.files.get('ppCode')
        if ppcode is None:
            wapp.Msg.error('ningún archivo seleccionado')
        else:
            fname, fext = os.path.splitext(ppcode.filename)
            wapp.Log.dbg('upload:', fname, fext)
            if fext != '.src' and fext != '.txt':
                wapp.Msg.error('sólo archivos .src o .txt son aceptados')
            else:
                wapp.Sess.writeFile('editor.src', ppcode.file.read().decode())
                wapp.Msg.info('archivo abierto satisfactoriamente')
                return wapp.Redirect('/')
    return wapp.Render()


@wapp.get('/upload/')
def upload():
    wapp.Start(tmpl='upload.html')
    return wapp.Render()


@wapp.post('/')
def indexPost():
    wapp.Start()
    ppCode = wapp.Req.forms.get('ppCode', '')
    wapp.Log.dbg("ppCode:", ppCode)

    if wapp.Req.POST.wappCmd == 'abrir':
        return wapp.Redirect('/upload/')

    elif wapp.Req.POST.wappCmd == 'borrar':
        wapp.Sess.writeFile('editor.src', '')
        tdata = {
            'wappEditorSrc': '',
        }
        return wapp.Render(tmplData=tdata)

    elif ppCode == '':
        wapp.Msg.error('el archivo está vacio')
        return wapp.Render()

    else:
        if wapp.Req.POST.wappCmd == 'guardar':
            return wapp.CodeSave(ppCode)

        elif wapp.Req.POST.wappCmd == 'ejecutar':
            return wapp.Render(tmpl='exec.html')

        else:
            return wapp.Render()


@wapp.get('/')
def index():
    wapp.Start()
    try:
        ppcode = wapp.Sess.readFile('editor.src')
    except Exception as e:
        wapp.Log.dbg('Exception:', e)
        ppcode = ''
    tdata = {
        'wappEditorSrc': ppcode,
    }
    return wapp.Render(tmplData=tdata)
