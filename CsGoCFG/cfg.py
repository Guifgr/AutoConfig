import os
import urllib.request

def findCSFolder():
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" ]
    for letter in letters:
        actual = letter
        print("Searching for CSGO Folder in disk",letter)

        for root, subdirs,files in os.walk(actual+':\\'):
            for d in subdirs:
                if d == "Counter-Strike Global Offensive":
                    path = root +"\\"+ d
                    return path

def findCfgFolder(csPath):
    for root, subdirs,files in os.walk(csPath+"\\"):
            for d in subdirs:
                if d == "cfg":
                    path = root +"\\"+ d
                    return path

def autoexecExists(findCfgFolder):
    path = False
    for root, subdirs,files in os.walk(csPath+"\\"):
            for d in files:
                if d == "autoexec.cfg":
                    path = root +"\\"+ d
                    return path

try:
    name = input("Digite o nome do player\n").upper()
    with urllib.request.urlopen('https://guilhermefgr.com.br/tests/CS_'+name+'.txt') as f:
        cfg = f.read().decode('ISO-8859-1')

    csPath = findCSFolder()
    print(csPath)

    findCfgFolder = findCfgFolder(csPath)
    print(findCfgFolder)

    autoexecPath = autoexecExists(findCfgFolder)
    if(autoexecPath == None):
        f = open(findCfgFolder+"\\autoexec.cfg", "w")
        print("Created file")
        print(findCfgFolder+"\\autoexec.cfg")
        open(findCfgFolder+"\\autoexec.cfg",'w').write(cfg)
    else:
        print(autoexecPath)
        open(autoexecPath,'w').write(cfg)

except:
    print("User not Found 404")