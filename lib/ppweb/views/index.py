from .. import wapp

@wapp.get('/')
def index():
    return wapp.Render()


@wapp.get('/static/<filename:path>')
def sendFile(filename):
    return wapp.SendFile(filename)


@wapp.post('/exec/')
def codeExec():
    return wapp.Render()
