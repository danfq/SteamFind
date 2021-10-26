#SteamFind v1.0.0
#DanFQ

#Requirements
import os
from colorama import Fore
import argparse
import signal
import sys
from bin.util import Util

#Arguments
parser = argparse.ArgumentParser(usage = Util.steamFindBanner())

parser.add_argument("--start", help = "First Steam AppID", type = int)
parser.add_argument("--end", help = "Final Steam AppID", type = int)
parser.add_argument("--id", help = "Steam AppID", type = int)
parser.add_argument("--name", help = "Steam App Name", type = str)
parser.add_argument("--gui", help = "Launch in GUI Mode", action = "store_true")

arguments = parser.parse_args()

#CTRL+C
def signalHandler(signal, frame):
    print(Fore.LIGHTYELLOW_EX + "\n\n\n [*] CTRL+C Detected. Exiting.\n\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)

#Run
os.system("cls")
Util.steamFindBanner()

if (arguments.start and arguments.end):
    Util.createIDList(int(arguments.start), int(arguments.end))
elif (arguments.id):
    Util.specificIDLookup(arguments.id)
elif (arguments.name):
    Util.queryLookup(arguments.name)
elif (arguments.gui):
    Util.launchGUI()
else:
    Util.mainMenu()