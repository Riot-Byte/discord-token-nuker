import requests, json, colorama
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

    response = requests.get("https://discord.com/api/v10/users/@me/relationships", headers=headers)
    
    print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Loaded response text {Fore.BLUE}{response.text}\n")
    
    if response.status_code == 200:
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to decode response JSON")
            return
        
        friend_info_to_remove = [(friend["id"], friend["user"]["username"]) for friend in response_json]

        for friend_id, friend_username in friend_info_to_remove:
            response = requests.delete(f"https://discord.com/api/v10/users/@me/relationships/{friend_id}", headers=headers)
            
            if response.status_code == 204:
                print(f"{Fore.WHITE}{ctime()} {Fore.MAGENTA}Friend '{friend_username}' removed successfully")
            else:
                print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to remove friend '{friend_username}' | {str(response.status_code)}")
        print(f"\n{Fore.WHITE}{ctime()} {Fore.MAGENTA}Successfully removed all friends\n")
    
    elif response.status_code == 401:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Invalid token.")
    else:
        print(f"{Fore.WHITE}{ctime()} {Fore.RED}Failed to fetch relationships | {response.status_code}")