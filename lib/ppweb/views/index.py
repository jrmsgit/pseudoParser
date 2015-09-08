from .. import wapp

@wapp.get('/')
def index():
    return wapp.render()


@wapp.get('/static/<filename:path>')
def send_file(filename):
    return wapp.send_file(filename)


@wapp.post('/exec/')
def codeExec():
    return wapp.render()
