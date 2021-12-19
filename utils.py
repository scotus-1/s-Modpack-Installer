from os import path
import json


# Load or create local config file
def configLoad():
    if path.exists('../s_modpack_installer/smi_config.json'):
        print(' [+] Found .\\smi_config.json, now loading settings')
        with open('../s_modpack_installer/smi_config.json', 'r') as config_file:
            return json.load(config_file)
    else:
        print(' [-] Did not find .\\smi_config.json, running first time initialization \n')
        return firstTimeInit()


# First Time Init
def firstTimeInit():
    print("[*] Finding \\.minecraft\\mods folder, auto-checking user directory")
    modFolder = findModFolder()

    options = {"modFolder": modFolder}
    print("[*] Creating and writing config file")
    with open("../s_modpack_installer/smi_config.json", "w") as config_file:
        json.dump(options, config_file)

    return options


# Mod Folder Handle, add linux support for default?
def findModFolder():
    defaultModPath = path.expanduser("~") + '\\AppData\\Roaming\\.minecraft\\mods'

    modFolder = None
    if path.exists(defaultModPath):
        print(' [+] Found \\mods folder at ' + defaultModPath)
        modFolder = defaultModPath
    else:
        print(' [-] Did not find \\mods folder in ' + defaultModPath)
        validFolder = False
        while not validFolder:
            modFolder = input(' [-] Manually find and input new mods folder: ')
            if path.exists(modFolder):
                validFolder = True
                print(' [+] Valid Folder Inputted')
            else:
                print(' [-] Folder Not Found or Not Valid')

    return modFolder
