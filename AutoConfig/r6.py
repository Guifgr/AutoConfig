import os
import ctypes

if os.name == 'nt':
    import ctypes
    from ctypes import windll, wintypes
    from uuid import UUID

    # ctypes GUID copied from MSDN sample code
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ] 

        def __init__(self, uuidstr):
            uuid = UUID(uuidstr)
            ctypes.Structure.__init__(self)
            self.Data1, self.Data2, self.Data3, \
                self.Data4[0], self.Data4[1], rest = uuid.fields
            for i in range(2, 8):
                self.Data4[i] = rest>>(8-i-1)*8 & 0xff

    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID), wintypes.DWORD,
        wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
    ]

    def _get_known_folder_path(uuidstr):
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value

    FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'

    def get_download_folder():
        return _get_known_folder_path(FOLDERID_Download)
else:
    def get_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")


def findDocumentsFolder():
    from ctypes.wintypes import MAX_PATH
    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        return buf.value
    else:
        return None


def findMyGamesPath(documentsPath):
    for root, subdirs,files in os.walk(documentsPath+"\\"):
            for d in subdirs:
                if d == "My Games":
                    path = root +r""+ d
                    return path                    

def findR6Path(documentsPath):
    for root, subdirs,files in os.walk(documentsPath+"\\"):
            for d in subdirs:
                if d == "Rainbow Six - Siege":
                    path = root +r""+ d
                    return path


def GameSettingsPath(path, GameSettings):
    for root, subdirs,files in os.walk(path+"\\"):
            for d in files:
                if d == "GameSettings.ini":
                    path = root +"\\"+ d
                    open(path,'w').write(GameSettings)
                    print("Edited configs file in:"+path)

def r6(GameSettings):
    documentsPath = findDocumentsFolder()
    print(documentsPath)

    myGamesPath = findMyGamesPath(documentsPath)
    print(myGamesPath)

    R6Path = findR6Path(myGamesPath)
    print(R6Path)

    GameSettingsPath(R6Path, GameSettings)
    
    