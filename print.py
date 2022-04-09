from colorama import Fore

def print_error(text):
    print(f'{Fore.RED}ERROR: {text}{Fore.RESET}\n')

def print_hint(text):
    print(f'{Fore.BLUE}HINT: {text}{Fore.RESET}')

