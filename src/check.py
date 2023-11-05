import os, sys
from colorama import Fore, init
from time import sleep
from src import print_slow

def check_requirements():
    try:
        sleep(0.5)
        #check if the os have linux
        if os.name == "nt":
            init(convert=True)
            print_slow.slow_type(Fore.BLUE + "\n\nSystem:" + Fore.RED + " [Error 1]" + Fore.RESET)
            sys.exit()
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nSystem:" + Fore.GREEN + " [OK]")
    
        #check the installed tools
        sleep(0.2)
        if os.system("command -v aircrack-ng >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\nAircrack-ng" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nAircrack-ng" + Fore.RED + " [Error 2]" + Fore.RESET)
            sys.exit()
        sleep(0.2)
        if os.system("command -v mdk4 >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\nmdk4" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nmdk4" + Fore.RED + " [Error 2]" + Fore.RESET)
            sys.exit()
        if os.system("command -v nmcli >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\nnmcli" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nnmcli" + Fore.RED + " [Error 2]" + Fore.RESET)
            sys.exit()
        sleep(0.2)
    except SystemExit:
        sys.exit()
    except:
        print("\n[Error 1]")
        sys.exit()
