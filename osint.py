import phonenumbers
import requests
import whois
from colorama import Fore

def phone_lookup():
    number = input(Fore.YELLOW + "\nEnter phone number (with country code): ")
    try:
        parsed_number = phonenumbers.parse(number)
        print(Fore.GREEN + f"Country: {phonenumbers.region_code_for_number(parsed_number)}")
        print(Fore.GREEN + f"Valid: {phonenumbers.is_valid_number(parsed_number)}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def email_recon():
    email = input(Fore.YELLOW + "\nEnter email: ")
    response = requests.get(f"https://emailrep.io/{email}")
    if response.status_code == 200:
        data = response.json()
        print(Fore.GREEN + f"Reputation: {data['reputation']}")
    else:
        print(Fore.RED + "Email lookup failed.")

def whois_lookup():
    domain = input(Fore.YELLOW + "\nEnter domain: ")
    try:
        w = whois.whois(domain)
        print(Fore.GREEN + f"Registrar: {w.registrar}")
        print(Fore.GREEN + f"Creation Date: {w.creation_date}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def osint_menu():
    print(Fore.CYAN + "[1] Phone Number Lookup")
    print(Fore.CYAN + "[2] Email Recon")
    print(Fore.CYAN + "[3] WHOIS Lookup")
    choice = input(Fore.YELLOW + "\nChoose option: ")

    if choice == "1":
        phone_lookup()
    elif choice == "2":
        email_recon()
    elif choice == "3":
        whois_lookup()
    else:
        print(Fore.RED + "Invalid choice!")
