from tempfile import TemporaryFile

output = None

def progStart():
    global output
    if output is not None:
        output.close()
    output = TemporaryFile(mode='w+')
