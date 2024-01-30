import os, sys
from colorama import Fore
from source import logs

def monitor(iface):
    logs.log(0, "killing processes that can compromise mode switching")
    test = os.system("sudo airmon-ng check kill")
    if test == 0:
        logs.log(2, "processes killed")
        logs.log(0, "switching to monitor mode")
        test = os.system("sudo airmon-ng start " + iface)
        if test == 0:
            logs.log(2, "monitor mode enabled")
            print(Fore.GREEN + "\n[Monitor mode enabled]")
            input("[Press enter to continue]")
        else:
            logs.log(1, "[Error 3], failed switching to monitor mode")
            print(Fore.RED + "\n[Error 3]")
    else:
        logs.log(1, "[Error 3], failed killing processes")
        print(Fore.RED + "\n[Error 3]")
        sys.exit()
    print(Fore.RESET)

def managed(iface):
    logs.log(0, "switching to managed mode")
    test = os.system("sudo airmon-ng stop " + iface)
    if test == 0:
        test = os.system("sudo systemctl start NetworkManager")
        if test == 0:
            logs.log(2, "managed mode enabled; NetworkManager started")
            print(Fore.GREEN + "\n[Managed mode enabled + NetworkManager started]")
        else:
            logs.log(2, "managed mode enabled")
            print(Fore.GREEN + "\n[Managed mode enabled]")
        input("[Press enter to continue] ")
    else:
        logs.log(1, "[Error 3]; failed switching to monitor mode")
        print(Fore.RED + "\n[Error 3]")
        sys.exit()
    print(Fore.RESET)
