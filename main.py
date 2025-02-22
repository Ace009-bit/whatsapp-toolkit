import os
import time
from colorama import Fore, Style, init
import osint
import sms
import offensive

# Initialize colorama
init(autoreset=True)

# ASCII Banner
BANNER = """
{0}
@@@  @@@  @@@  @@@  @@@   @@@@@@   @@@@@@@   @@@@@@    @@@@@@   @@@@@@@   @@@@@@@  
@@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@ 
@@!  @@!  @@!  @@!  @@@  @@!  @@@    @@!    !@@       @@!  @@@  @@!  @@@  @@!  @@@ 
!@!  !@!  !@!  !@!  @!@  !@!  @!@    !@!    !@!       !@!  @!@  !@!  @!@  !@!  @!@ 
@!!  !!@  @!@  @!@!@!@!  @!@!@!@!    @!!    !!@@!!    @!@!@!@!  @!@@!@!   @!@@!@!  
!@!  !!!  !@!  !!!@!!!!  !!!@!!!!    !!!     !!@!!!   !!!@!!!!  !!@!!!    !!@!!!   
!!:  !!:  !!:  !!:  !!!  !!:  !!!    !!:         !:!  !!:  !!!  !!:       !!:      
:!:  :!:  :!:  :!:  !:!  :!:  !:!    :!:        !:!   :!:  !:!  :!:       :!:      
 :::: :: :::   ::   :::  ::   :::     ::    :::: ::   ::   :::   ::        ::      
  :: :  : :     :   : :   :   : :     :     :: : :     :   : :   :         :       
{1}
""".format(Fore.RED, Style.RESET_ALL)

# Main menu function
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(Fore.GREEN + "[1] OSINT Tools")
    print(Fore.GREEN + "[2] SMS Tools")
    print(Fore.GREEN + "[3] Offensive Security Tools")
    print(Fore.GREEN + "[4] Exit")
    
    choice = input(Fore.YELLOW + "\nSelect an option: ")

    if choice == "1":
        osint.osint_menu()
    elif choice == "2":
        sms.sms_menu()
    elif choice == "3":
        offensive.offensive_menu()
    elif choice == "4":
        print(Fore.RED + "\nExiting...")
        time.sleep(1)
        exit()
    else:
        print(Fore.RED + "\nInvalid choice! Try again.")
        time.sleep(1)
        main_menu()

# Run the main menu
if __name__ == "__main__":
    main_menu()
