import os, sys
from colorama import Fore
from src import print_slow

def ap(iface):
    command = os.system("sudo mdk4 " + iface + " b -f aps.txt")
    if command > 2 and command != 33280:
        print(Fore.RED + "\n[Error 8]" + Fore.RESET)
        sys.exit()
