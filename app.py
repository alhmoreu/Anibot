from Profile import Profile, ProfileNotCompleted, UnsuitableValue
import profile_module
import time_module
import calculation_module
import print_module
from inout import load
from sys import exit
from colorama import init

init()

WELCOME = """
/////////////////////////////
Welcome to Anibot, which module would you like to access? (Please, enter a number)

1. Profile
2. Time
3. Calculation
4. Print
5. Exit
/////////////////////////////
Option:
"""
SAVE_FILENAME = 'save.txt'
profile = Profile()
load(SAVE_FILENAME)

def exit_app():
    print("Exiting..\n")
    exit()


if __name__ == "__main__":

    options = {
        '1': profile_module.profile_module,
        '2': time_module.time_module,
        '3': calculation_module.calculation_module,
        '4': print_module.print_module,
        '5': exit_app
    }

    while True:
        answer = str(input(WELCOME))
        print("\n")
        try:
            options[answer]()
        except KeyError:
            print(" Please, enter a number (1-5)")

        except ProfileNotCompleted as err:
            print(err)

        except UnsuitableValue as err:
            print(err)