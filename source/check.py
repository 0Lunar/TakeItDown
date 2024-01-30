import os, sys
from colorama import Fore, init
from time import sleep
from source import print_slow, logs

def check_requirements():
    try:
        #check the os
        if os.name == "nt":
            init(convert=True)
            print_slow.slow_type(Fore.BLUE + "\n\nSystem:" + Fore.RED + " [Error 1]" + Fore.RESET)
            logs.log(1, "[Error 1]; Windows is not compatible with TakeItDown")
            sys.exit()
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nSystem:" + Fore.GREEN + " [OK]")
    
        #check the installed tools
        logs.log(0, "checking installed tools")
        sleep(0.2)
        #aircrack-ng
        if os.system("command -v aircrack-ng >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\nAircrack-ng" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nAircrack-ng" + Fore.RED + " [Error 2]" + Fore.RESET)
            logs.log(1, "[Error 2]; missing aircrack-ng")
            sys.exit()
        sleep(0.2)
        #mdk4
        if os.system("command -v mdk4 >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\nmdk4" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nmdk4" + Fore.RED + " [Error 2]" + Fore.RESET)
            logs.log(1, "[Error 2]; missing mkd4")
            sys.exit()
        #nmcli
        if os.system("command -v nmcli >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\nnmcli" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\nnmcli" + Fore.RED + " [Error 2]" + Fore.RESET)
            logs.log(1, "[Error 2]; missing nmcli")
            sys.exit()
        #arp-scan
        if os.system("command -v arp-scan >/dev/null 2>&1") == 0:
            print_slow.slow_type(Fore.BLUE + "\n\narp-scan" + Fore.GREEN + " [OK]")
        else:
            print_slow.slow_type(Fore.BLUE + "\n\narp-scan" + Fore.RED + " [Error 2]" + Fore.RESET)
            logs.log(1, "[Error 2]; missing arp-scan")
            sys.exit()
        sleep(0.2)
        logs.log(2, "all requirements installed")
    except PermissionError:
        print_slow.slow_type(Fore.BLUE + "\n\nLogFile" + Fore.RED + " [Error 12]")
        sys.exit()
    except SystemExit:
        logs.log(0, "System Exit")
        sys.exit()
    except KeyboardInterrupt:
        logs.log(0, "Keyboard Interrupt detected during check tools, exiting")
        sys.exit()
    except:
        logs.log(1, "[Error 404], unexpected error")
        print("\n[Error 404]")
        sys.exit()
