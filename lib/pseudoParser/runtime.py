from tempfile import TemporaryFile

output = None
inputCmd = None

def progStart():
    global output
    if output is not None:
        output.close()
    output = TemporaryFile(mode='w+')

def printOutput():
    global output
    output.seek(0, 0)
    for l in output.readlines():
        print(l, end='')
