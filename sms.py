import requests
import time
import json
from colorama import Fore, Style
from twilio.rest import Client

# API Keys (Replace with your own)
TEXTBELT_API_KEY = "your_textbelt_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE = "your_twilio_phone_number"
TWILIO_WHATSAPP = "whatsapp:+14155238886"  # Twilio Sandbox Number

# Initialize Twilio Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Logging System - Saves Sent Messages
def log_message(service, recipient, message):
    with open("sent_messages.log", "a") as log:
        log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {service} -> {recipient}: {message}\n")

# SMS Bomber - Sends multiple SMS to your own number
def sms_bomber():
    number = input(Fore.YELLOW + "\nEnter your phone number (for testing only): ")
    message = input(Fore.YELLOW + "Enter message to spam: ")
    count = int(input(Fore.YELLOW + "Enter number of messages: "))

    for i in range(count):
        response = requests.post("https://textbelt.com/text", {
            'phone': number,
            'message': message,
            'key': TEXTBELT_API_KEY,
        })
        data = response.json()

        if data.get("success"):
            print(Fore.GREEN + f"Sent [{i+1}/{count}] to {number}")
            log_message("SMS Bomber", number, message)
        else:
            print(Fore.RED + f"Failed to send SMS: {data.get('error', 'Unknown error')}")

        time.sleep(1)

# SMS Spoofing - Requires a spoofing service API
def sms_spoof():
    sender = input(Fore.YELLOW + "\nEnter fake sender name: ")
    receiver = input(Fore.YELLOW + "Enter recipient phone number: ")
    message = input(Fore.YELLOW + "Enter message: ")

    response = requests.post("https://spoofmytextmessage.com/api/send", {
        'api_key': "your_spoofing_api_key",
        'from': sender,
        'to': receiver,
        'text': message,
    })
    data = response.json()

    if data.get("success"):
        print(Fore.GREEN + f"Spoofed SMS sent from {sender} to {receiver}")
        log_message("SMS Spoof", receiver, message)
    else:
        print(Fore.RED + f"SMS spoofing failed: {data.get('error', 'Unknown error')}")

# Bulk SMS Sender (Twilio)
def bulk_sms():
    message = input(Fore.YELLOW + "\nEnter the message for bulk sending: ")
    contacts = input(Fore.YELLOW + "Enter phone numbers (comma-separated): ").split(',')

    for number in contacts:
        try:
            sms = client.messages.create(
                body=message,
                from_=TWILIO_PHONE,
                to=number.strip()
            )
            print(Fore.GREEN + f"Bulk SMS sent to {number.strip()} - SID: {sms.sid}")
            log_message("Bulk SMS", number.strip(), message)
        except Exception as e:
            print(Fore.RED + f"Failed to send SMS to {number.strip()}: {str(e)}")

# WhatsApp Bomber
def whatsapp_bomber():
    number = input(Fore.YELLOW + "\nEnter your WhatsApp number (with country code, e.g., +91XXXXXXXXXX): ")
    message = input(Fore.YELLOW + "Enter message to spam: ")
    count = int(input(Fore.YELLOW + "Enter number of messages: "))

    for i in range(count):
        try:
            sms = client.messages.create(
                body=message,
                from_=TWILIO_WHATSAPP,
                to=f"whatsapp:{number.strip()}"
            )
            print(Fore.GREEN + f"WhatsApp Message [{i+1}/{count}] sent to {number} - SID: {sms.sid}")
            log_message("WhatsApp Bomber", number, message)
        except Exception as e:
            print(Fore.RED + f"Failed to send WhatsApp message: {str(e)}")

        time.sleep(1)

# WhatsApp Spoofing
def whatsapp_spoof():
    sender = input(Fore.YELLOW + "\nEnter fake sender name: ")
    receiver = input(Fore.YELLOW + "Enter recipient WhatsApp number: ")
    message = input(Fore.YELLOW + "Enter message: ")

    response = requests.post("https://spoofmytextmessage.com/api/send", {
        'api_key': "your_spoofing_api_key",
        'from': sender,
        'to': f"whatsapp:{receiver.strip()}",
        'text': message,
    })
    data = response.json()

    if data.get("success"):
        print(Fore.GREEN + f"Spoofed WhatsApp message sent from {sender} to {receiver}")
        log_message("WhatsApp Spoof", receiver, message)
    else:
        print(Fore.RED + f"WhatsApp spoofing failed: {data.get('error', 'Unknown error')}")

# WhatsApp Bulk Sender
def whatsapp_bulk():
    message = input(Fore.YELLOW + "\nEnter the WhatsApp message for bulk sending: ")
    contacts = input(Fore.YELLOW + "Enter phone numbers (comma-separated, with country codes): ").split(',')

    for number in contacts:
        try:
            sms = client.messages.create(
                body=message,
                from_=TWILIO_WHATSAPP,
                to=f"whatsapp:{number.strip()}"
            )
            print(Fore.GREEN + f"WhatsApp message sent to {number.strip()} - SID: {sms.sid}")
            log_message("WhatsApp Bulk", number.strip(), message)
        except Exception as e:
            print(Fore.RED + f"Failed to send WhatsApp message to {number.strip()}: {str(e)}")

# SMS Menu
def sms_menu():
    print(Fore.CYAN + "\n[1] SMS Bomber (Your Own Number Only)")
    print(Fore.CYAN + "[2] SMS Spoofing (Where Legally Allowed)")
    print(Fore.CYAN + "[3] Bulk SMS Sender")
    print(Fore.CYAN + "[4] WhatsApp Menu")
    print(Fore.CYAN + "[5] Back to Main Menu")

    choice = input(Fore.YELLOW + "\nChoose an option: ")

    if choice == "1":
        sms_bomber()
    elif choice == "2":
        sms_spoof()
    elif choice == "3":
        bulk_sms()
    elif choice == "4":
        whatsapp_menu()
    elif choice == "5":
        return
    else:
        print(Fore.RED + "Invalid choice!")

# WhatsApp Menu
def whatsapp_menu():
    print(Fore.CYAN + "\n[1] WhatsApp Bomber (Your Own Number Only)")
    print(Fore.CYAN + "[2] WhatsApp Spoofing (Where Legally Allowed)")
    print(Fore.CYAN + "[3] WhatsApp Bulk Sender")
    print(Fore.CYAN + "[4] Back to SMS Menu")

    choice = input(Fore.YELLOW + "\nChoose an option: ")

    if choice == "1":
        whatsapp_bomber()
    elif choice == "2":
        whatsapp_spoof()
    elif choice == "3":
        whatsapp_bulk()
    elif choice == "4":
        sms_menu()
    else:
        print(Fore.RED + "Invalid choice!")

# Run the SMS Menu
sms_menu()
