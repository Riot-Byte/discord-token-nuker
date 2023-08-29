import requests, threading, colorama
from time import sleep
from datetime import datetime
from colorama import Fore

colorama.init()

user_token = "."
server_avatar = "https://media.discordapp.net/attachments/1140304552562802799/1140306344696615002/riotadministration.png"
server_spam_amount = 10 # configure if you want

def ctime():
    return datetime.now().strftime("%H:%M:%S")

def create_server(server_name):
    headers = {
        "Authorization": f"{user_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"'
    }

    payload = {
        "name": server_name
    }

    response = requests.post("https://discord.com/api/v9/guilds", headers=headers, json=payload)

    if response.status_code == 201:
        server_data = response.json()
        server_id = server_data["id"]
        set_avatar(server_id)
        print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Created server {Fore.BLUE}'{server_name}' {Fore.MAGENTA}with ID {server_id}")
    elif response.status_code == 429:
        retry_after = response.json()["retry_after"] + 0.1
        sleep(retry_after)
        newresponse = requests.post("https://discord.com/api/v9/guilds", headers=headers, json=payload)
        if newresponse.status_code == 201:
            server_data = newresponse.json()
            server_id = server_data["id"]
            set_avatar(server_id)
            print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Created server {Fore.BLUE}'{server_name}' {Fore.MAGENTA}with ID {server_id}")
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to create server {Fore.BLUE}'{server_name}' {Fore.RED}| {response.status_code}")

def set_avatar(server_id):
    headers = {
        "Authorization": f"{user_token}"
    }

    payload = {
        "icon": server_avatar
    }

    response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers, json=payload)

    if response.status_code == 204:
        print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Set server avatar for server ID {Fore.BLUE}{server_id}")
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to set server avatar for server ID {Fore.BLUE}{server_id} {Fore.RED}| {response.status_code}")

def start():
    for i in range(server_spam_amount):
        create_server("NUKED")