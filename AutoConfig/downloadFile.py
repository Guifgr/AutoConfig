import urllib.request
def downloadGameFile(game, name):
  
    with urllib.request.urlopen('https://guifgr.com/tests/'+game+'_'+name+'.txt') as f:
        fileTxt = f.read().decode('ISO-8859-1')

        return fileTxt
