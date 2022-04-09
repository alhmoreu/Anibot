# Print Module

import app
from strings import TASK, PRINT_MENU, OPTIONS_ERROR, REQUESTING_NAME


def print_surname_name():
    print(f'{app.profile.surname}, {app.profile.name}')


def print_age():
    print(f'You have <{app.profile.age}> years')
    if app.profile.age < 35:
        print('Congratulations! You are very young!')


print_options = {
    's': print_surname_name,
    'a': print_age
}


def print_module():
    while True:
        print_answer = input(f'\n{TASK} {PRINT_MENU}')
        # 'e' option exits print module
        if print_answer == 'e':
            break

        try:
            print_options[print_answer]()
        except KeyError:
            print(OPTIONS_ERROR)