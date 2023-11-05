import os, sys
from colorama import Fore

def monitor(iface):
    test = os.system("sudo airmon-ng check kill")
    if test == 0:
        test = os.system("sudo airmon-ng start " + iface)
        if test == 0:
            print(Fore.GREEN + "\n[Monitor mode enabled]")
            input("[Press enter to continue]")
        else:
            print(Fore.RED + "\n[Error 3]")
    else:
        print(Fore.RED + "\n[Error 3]")
        sys.exit()
    print(Fore.RESET)

def managed(iface):
    test = os.system("sudo airmon-ng stop " + iface)
    if test == 0:
        test = os.system("sudo systemctl start NetworkManager")
        if test == 0:
            print(Fore.GREEN + "\n[Monitor mode enabled + NetworkManager started]")
        else:
            print(Fore.GREEN + "\n[Monitor mode enabled]")
        input("[Press enter to continue] ")
    else:
        print(Fore.RED + "\n[Error 3]")
        sys.exit()
    print(Fore.RESET)
