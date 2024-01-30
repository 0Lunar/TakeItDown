from colorama import Fore
import os
from source import print_slow, logs

def arpScan(iface, option):
    optionError = 0
    if option == 1:
        l = "starting arp scan on " + iface + " (list)"
        logs.log(0, l)
        command = "sudo arp-scan -l -I " + iface
    elif option == 2:
        l = "starting arp scan on " + iface + " (list verbose)"
        logs.log(0, l)
        command = "sudo arp-scan -l -v -I " + iface
    elif option == 3:
        l = "starting arp scan on " + iface + " (list quiet)"
        logs.log(0, l)
        command = "sudo arp-scan -l -q -I " + iface
    else:
        logs.log(1, "[Error 9]; option not found")
        print(Fore.RED + "[Error 9]" + Fore.RESET)
        optionError = 1

    if optionError == 0:
        print(Fore.BLUE + "\n\n--------------- ARP SCAN ---------------\n" + Fore.CYAN)
        command = os.system(command)
        if command != 0:
            logs.log(1, "[Error 13]; arp-scan error")
            print(Fore.RED + "[Error 13]" + Fore.RESET)
            sys.exit()
        input(Fore.GREEN + "\n\n[Press enter to continue]" + Fore.RESET)
        logs.log(2, "arp scan completed")
