import requests
from colorama import Fore

SHODAN_API_KEY = "your_shodan_api_key"

def shodan_lookup():
    ip = input(Fore.YELLOW + "\nEnter IP address: ")
    response = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}")

    if response.status_code == 200:
        print(Fore.GREEN + response.json())
    else:
        print(Fore.RED + "Error fetching data from Shodan.")

def offensive_menu():
    print(Fore.CYAN + "[1] Shodan Lookup")
    choice = input(Fore.YELLOW + "\nChoose option: ")

    if choice == "1":
        shodan_lookup()
    else:
        print(Fore.RED + "Invalid choice!")
