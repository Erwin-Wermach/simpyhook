import requests
import colorama
from colorama import Fore, Back, Style

print(Fore.BLUE + """
     _                       _                 _    
 ___(_)_ __ ___  _ __  _   _| |__   ___   ___ | | __
/ __| | '_ ` _ \\| '_ \\| | | | '_ \\ / _ \\ / _ \\| |/ /
\__ \ | | | | | | |_) | |_| | | | | (_) | (_) |   < 
|___/_|_| |_| |_| .__/ \__, |_| |_|\___/ \___/|_|\_\\
                |_|    |___/                        
""")
print(Style.RESET_ALL)
webhook = input(Fore.WHITE + "Your Webhook Url: ")
message = input(Fore.WHITE + "Your Message: ")
print(Style.RESET_ALL)

r = requests.post(webhook, json={'content': message})
if r.status_code == 204:
    print(Fore.GREEN +"Message Send to Webhook!")
    print(Style.RESET_ALL)
else:
    print(Fore.RED + f"Sending Message to Webhook failed with status code: {r.status_code}")
    print(Style.RESET_ALL)