from utils import *

def preRun():
    print("[*] Checking for config file")
    return configLoad()



def info():
    print("""
    ███████╗    ███╗   ███╗    ██╗
    ██╔════╝    ████╗ ████║    ██║
    ███████╗    ██╔████╔██║    ██║
    ╚════██║    ██║╚██╔╝██║    ██║
    ███████║██╗ ██║ ╚═╝ ██║██╗ ██║██╗
    ╚══════╝╚═╝ ╚═╝     ╚═╝╚═╝ ╚═╝╚═╝
    """)


def options():
    pass

if __name__ == "__main__":
    preRun()
    info()
    print()

    while True:
        options()
