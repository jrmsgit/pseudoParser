from .. import wapp
from pseudoParser import runtime
from pseudoParser.compiler import parser
from pseudoParser.interpreter import runprog


@wapp.get('/exec/')
def program():
    wapp.Start(tmpl='exec.html')
    return wapp.Render()


@wapp.post('/exec/')
def progExec():
    wapp.Start(tmpl='exec.html')
    wapp.Log.dbg('progExec')

    tdata = {
        'wappExecOutput': list(),
    }

    if wapp.Req.POST.wappCmd == 'ejecutar':
        ppCode = wapp.Sess.readFile('editor.src')
        prog = parser.parse(ppCode)
        runprog(prog)
        runtime.output.seek(0, 0)
        tdata['wappExecOutput'] = runtime.output.readlines()

    return wapp.Render(tmplData=tdata)
