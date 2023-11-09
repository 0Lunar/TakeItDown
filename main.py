#!/usr/bin/python3

import os, sys
from colorama import Fore, init
from src import check, banner, mode, print_slow, deauth, ap, flood, logs, arpScan

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
        l = "choise: " + str(choise)
        logs.log(0, l)
        if choise == 1 or choise == 2:
            clean()
            banner.banner()
            print_slow.slow_type("\n  Enter one of these ifcaes\n\n")
            show_ifaces()
            iface = input("\n ==> ")
            l = "iface: ", iface
            logs.log(0, l)
            if choise == 1: #monitor mode
                mode.monitor(iface)
            else: #managed mode
                mode.managed(iface)
        elif choise == 3: #wifi list
            print("\n")
            if os.system("nmcli dev wifi") != 0:
                logs.log(1, "[Error 5]; nmcli error")
                print(Fore.RED , "\n[Error 5]" , Fore.RESET)
                sys.exit()
            else:
                logs.log(2, "nmcli executed")
                input(Fore.GREEN + "\n[Press enter to continue]" + Fore.RESET)
        elif choise == 4 or choise == 5: #deauth
            clean()
            banner.banner()
            logs.log(0, "deauth menu started")
            print_slow.slow_type(Fore.CYAN + "\n  Enter one of these ifaces\n\n")
            show_ifaces()
            iface = input(Fore.GREEN + "\n ==> " +Fore.YELLOW)
            l = "deauth iface: " + iface
            logs.log(0, l)
            deauth.scan(iface)
            bssid = input(Fore.GREEN + "\nEnter the bssid: " + Fore.YELLOW)
            l = "BSSID: " + bssid
            logs.log(0, l)
            if choise == 4:
                deauth.deauth(iface, bssid)
            else:
                deauth.advancedScan(iface, bssid)
                mac = input(Fore.GREEN + "\nEnter the mac: " + Fore.YELLOW)
                l = "MAC: " + mac
                logs.log(0, l)
                deauth.deauthdv(iface, bssid, mac)
        elif choise == 6: #spam ap
            clean()
            banner.banner()
            print_slow.slow_type(Fore.CYAN + "\n  Enter one of these ifaces\n\n")
            show_ifaces()
            iface = input(Fore.GREEN + "\n ==> " + Fore.YELLOW)
            l = "iface: " + iface
            logs.log(0, l)
            clean()
            banner.banner()
            print(Fore.CYAN + "\n\n---------------AP SPAM---------------" + Fore.GREEN)
            ap.ap(iface)
        elif choise == 7:
            print_slow.slow_type(Fore.GREEN + "\n\nEnter the ip: ")
            ip = input()
            l = "ip: " + ip
            logs.log(0, l)
            print_slow.slow_type("\n\nEnter the port: ")
            port = int(input())
            l = "port: " + str(port)
            logs.log(0, l)
            print(Fore.RESET)
            clean()
            banner.banner()
            flood.flood(ip, port)
        elif choise == 8:
            logss = open(logs.logFile(), "r")
            print("\n\n" + logss.read())
            print("\n\n" + Fore.GREEN + "[Press enter to continue]" + Fore.RESET)
            input()
        elif choise == 9:
            print(Fore.CYAN + "\nEnter the type of scan:" + Fore.GREEN + "\n\n 1. normal\n 2. verbose\n 3. qiet")
            arpOption = int(input("\n ==> " + Fore.YELLOW))
            l = "option: " + str(arpOption)
            logs.log(0, l)
            print(Fore.CYAN + "\n")
            show_ifaces()
            iface = input(Fore.GREEN + "\nEnter the iface: ")
            l = "iface: " + iface
            logs.log(0, l)
            arpScan.arpScan(iface, arpOption)
        elif choise == 10:
            clean()
            banner.banner()
            logs.log(1, "exiting")
            print_slow.slow_type("\n\nBye ;)\n\n")
            sys.exit()
        else:
            logs.log(1, "[Error 9]; command not found")
            print(Fore.RED , "[Error 9]" , Fore.RESET)
    except KeyboardInterrupt:
        logs.log(0, "Keyboard Interrupt detected, exiting")
        print(Fore.BLUE + "\n\n[WARNING] Keyboard Interrupt rilevated, exiting...")
        sys.exit()
    except SystemExit:
        logs.log(0, "System Exit")
        sys.exit()
    except ValueError:
        logs.log(1, "ValueError")
        pass
    except:
        logs.log(1, "[Error 404] unexpected error")
        print(Fore.RED , "\n[Error 404]" , Fore.RESET)
        sys.exit()

if __name__ == "__main__":
    clean()
    banner.banner()
    logs.startLog()
    check.check_requirements()
    print_slow.slow_type(Fore.GREEN + "\n\nAll ready, press enter to continue " + Fore.RESET)
    input()
    while(True):
        main()
