import requests, colorama, threading
from time import sleep
from datetime import datetime
from colorama import Fore

colorama.init()

user_token = "s-s-s-spe-spe-spe..."

def ctime():
    return datetime.now().strftime("%H:%M:%S")

def start():
    headers = {
        "Authorization": f"{user_token}"
    }

    response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)

    print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Loaded response text {Fore.BLUE}{response.text}\n")

    sleep(1)

    if response.status_code == 200:
        server_data = response.json()

        for server in server_data:
            server_id = server["id"]
            server_name = server["name"]
            is_owner = server["owner"]

            if is_owner:
                delete_response = requests.delete(f"https://discord.com/api/v10/guilds/{server_id}", headers=headers)
                if delete_response.status_code == 204:
                    print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Deleted server {Fore.BLUE}'{server_name}' {Fore.MAGENTA}successfully")
                elif delete_response.status_code == 429:
                    print(f"{Fore.WHITE}{ctime()} {Fore.YELLOW}Rate limited, waiting for 2 seconds...")
                    sleep(2)
                    new_delete_response = requests.delete(f"https://discord.com/api/v10/users/@me/guilds/{server_id}", headers=headers)
                    if new_delete_response.status_code == 204:
                        print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Left server {Fore.BLUE}'{server_name}' {Fore.MAGENTA}successfully")
                    else: continue
                else:
                    print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to delete server {Fore.BLUE}'{server_name}' {Fore.RED}| {delete_response.status_code}")
            else:
                leave_response = requests.delete(f"https://discord.com/api/v10/users/@me/guilds/{server_id}", headers=headers)
                if leave_response.status_code == 204:
                    print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Left server {Fore.BLUE}'{server_name}' {Fore.MAGENTA}successfully")
                elif leave_response.status_code == 429:
                    print(f"{Fore.WHITE}{ctime()} {Fore.YELLOW}Rate limited, waiting for 2 seconds...")
                    sleep(2)
                    new_leave_response = requests.delete(f"https://discord.com/api/v10/users/@me/guilds/{server_id}", headers=headers)
                    if new_leave_response.status_code == 204:
                        print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Left server {Fore.BLUE}'{server_name}' {Fore.MAGENTA}successfully")
                    else: continue
                else:
                    print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to leave server {Fore.BLUE}'{server_name}' {Fore.RED}| {leave_response.status_code}")
        print(f"\n{Fore.WHITE}{ctime()} {Fore.MAGENTA}Successfully left all servers\n")

    elif response.status_code == 401:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Invalid token.")
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to fetch relationships, status code {response.status_code}")