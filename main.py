#!/usr/bin/python3

import os, sys
from colorama import Fore, init
from src import check, banner, mode, print_slow, deauth, ap, flood

def clean():
    os.system("clear")

def show_ifaces():
    if os.system("ifconfig -a | sed 's/[ \\t].*//;/^$/d' | tr -d \":\" 1>/dev/null 2>/dev/null") != 0:
        printf("\n[Error 4]")
        sys.exit()
    else:
        os.system("ifconfig -a | sed 's/[ \\t].*//;/^$/d' | tr -d \":\"")

def main():
    try:
        clean()
        banner.banner()
        banner.commands()
        choise = int(input("\n\n ==> "))
        if choise == 1 or choise == 2:
            clean()
            banner.banner()
            print_slow.slow_type("\n  Enter one of these ifcaes\n\n")
            show_ifaces()
            iface = input("\n ==> ")
            if choise == 1: #monitor mode
                mode.monitor(iface)
            else: #managed mode
                mode.managed(iface)
        elif choise == 3: #wifi list
            if os.system("nmcli dev wifi") != 0:
                print(Fore.RED + "\n[Error 5]" + Fore.RESET)
                sys.exit()
            else:
                input("\nPress Enter to continue...")
        elif choise == 4 or choise == 5: #deauth
            clean()
            banner.banner()
            print_slow.slow_type("\n  Enter one of these ifaces\n\n")
            show_ifaces()
            iface = input("\n ==> ")
            deauth.scan(iface)
            bssid = input("\nEnter the bssid: ")
            if choise == 4:
                deauth.deauth(iface, bssid)
            else:
                deauth.advancedScan(iface, bssid)
                mac = input("\nEnter the mac: ")
                deauth.deauthdv(iface, bssid, mac)
        elif choise == 6: #spam ap
            clean()
            banner.banner()
            print_slow.slow_type("\n  Enter one of these ifaces\n\n")
            show_ifaces()
            iface = input("\n ==> ")
            ap.ap(iface)
        elif choise == 7:
            print_slow.slow_type("\n\nEnter the ip: ")
            ip = input()
            print_slow.slow_type("\n\nEnter the port: ")
            port = int(input())
            clean()
            banner.banner()
            flood.flood(ip, port)
        elif choise == 8:
            clean()
            banner.banner()
            print_slow.slow_type("\n\nBye ;)\n\n")
            sys.exit()
        else:
            print(Fore.RED + "[Error 9]" + Fore.RESET)
    except KeyboardInterrupt:
        print(Fore.BLUE + "\n[WARNING] Keyboard Interrupt rilevated, exiting...")
        sys.exit()
    except SystemExit:
        sys.exit()
    except ValueError:
        pass
    except:
        print(Fore.RED + "\n[Error 404]" + Fore.RESET)
        sys.exit()

if __name__ == "__main__":
    clean()
    banner.banner()
    check.check_requirements()
    print_slow.slow_type(Fore.GREEN + "\n\nAll ready, press enter to continue" + Fore.RESET)
    input()
    while(True):
        main() 
