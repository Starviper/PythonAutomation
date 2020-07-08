import traceback


def spam():
    bacon()


def bacon():
    try:
        raise Exception('This is the error message.')

    except:
        errorFile = open('Errorinfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')


spam()