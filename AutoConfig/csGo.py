import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
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

def autoexecExists(csPath):
    for root, subdirs,files in os.walk(csPath+"\\"):
            for d in files:
                if d == "autoexec.cfg":
                    path = root +"\\"+ d
                    return path

def csGo(cfg):
    csPath = findCSFolder()
    print(csPath)

    cfgFolder = findCfgFolder(csPath)
    print(cfgFolder)

    autoexecPath = autoexecExists(cfgFolder)
    if(autoexecPath == None):
        open(cfgFolder+"\\autoexec.cfg",'w').write(cfg)
        print(bcolors.OKGREEN+"Created file in:"+cfgFolder+"\\autoexec.cfg"+bcolors.ENDC)
    else:
        open(cfgFolder+"\\autoexec.cfg",'w').write(cfg)
        print(bcolors.OKGREEN+"Recreated file in:"+cfgFolder+"\\autoexec.cfg"+bcolors.ENDC)
        