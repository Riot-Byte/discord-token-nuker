import requests, colorama
from colorama import Fore
from time import sleep
from datetime import datetime

colorama.init()

user_token = "..."

def ctime():
    return datetime.now().strftime("%H:%M:%S")

def leave_channel(channel_id):
    headers = {
        "Authorization": f"{user_token}"
    }

    response = requests.delete(f"https://discord.com/api/v10/channels/{channel_id}", headers=headers)

    if response.status_code == 200:
        print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Left channel {Fore.BLUE}'{channel_id}' {Fore.MAGENTA}successfully")
    elif response.status_code == 429:
        print(f"{Fore.WHITE}{ctime()} {Fore.YELLOW}Rate limited, waiting for 2 seconds...")
        sleep(2)
        leave_channel(channel_id)
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to leave channel {Fore.BLUE}'{channel_id}' {Fore.RED}| {response.status_code}")

def remove_dm(dm_id):
    headers = {
        "Authorization": f"{user_token}"
    }

    response = requests.delete(f"https://discord.com/api/v10/channels/{dm_id}", headers=headers)

    if response.status_code == 200:
        print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Removed DM {Fore.BLUE}'{dm_id}' {Fore.MAGENTA}successfully")
    elif response.status_code == 429:
        print(f"{Fore.WHITE}{ctime()} {Fore.YELLOW}Rate limited, waiting for 2 seconds...")
        sleep(2)
        remove_dm(dm_id)
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to remove DM {Fore.BLUE}'{dm_id}' {Fore.RED}| {response.status_code}")

def start():
    headers = {
        "Authorization": f"{user_token}"
    }

    response = requests.get("https://discord.com/api/v10/users/@me/channels", headers=headers)

    if response.status_code == 200:
        channel_data = response.json()

        for channel in channel_data:

            if channel["type"] == 3:
                leave_channel(channel["id"])
            elif channel["type"] == 1:
                remove_dm(channel["id"])
        print(f"\n{Fore.WHITE}{ctime()} {Fore.MAGENTA}Successfully removed all DMs\n")
    elif response.status_code == 401:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Invalid token.")
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to fetch DMs, status code {response.status_code}")