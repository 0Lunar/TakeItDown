import os
from datetime import datetime
from src import print_slow
from colorama import Fore

INFO = datetime.now().strftime("%d:%m:%Y %H:%M:%S") + " [INFO] "
ERROR = datetime.now().strftime("%d:%m:%Y %H:%M:%S") + " [ERROR] "
SUCCESS = datetime.now().strftime("%d:%m:%Y %H:%M:%S") + " [SUCCESS] "

def logFile():
    currentDir = os.getcwd()
    logFile = currentDir + "/logs.log"
    return logFile

def log(mode, logText):
    logfile = open(logFile(), "a+")
    logsType = [INFO, ERROR, SUCCESS]
    if mode < 0 or mode > 2:
        logfile.writelines(ERROR + " Invalid mode for function: logs.log(" + mode + ")")
    else:
        logfile.writelines(("\n" + logsType[mode] + str(logText)))
    logfile.close()

def startLog():
    try:
        #make log file
        if(os.path.isfile(logFile()) == False):
            logfile = open(logFile(), "w")
            print_slow.slow_type(Fore.BLUE + "\n\nLogFile" + Fore.GREEN + " [CREATED]")
            logfile.write("----------" + datetime.now().strftime("%d:%m:%Y %H:%M:%S") + " Log File created----------\n")
        else:
            logfile = open(logFile(), "a+")
            logfile.writelines("\n\n----------" + datetime.now().strftime("%d:%m:%Y %H:%M:%S") + " Log File created----------\n")
            print_slow.slow_type(Fore.BLUE + "\n\nLogFile" + Fore.GREEN + " [OK]")
    except PermissionError:
        print(Fore.RED + "[Error 12]")