# Calculation Module

import app
from strings import CALCULATION_MENU, TASK, OPTIONS_ERROR, VOWELS_NAME, VOWELS_SURNAME, REQUESTING_NAME


def length_name():
    user_name = app.profile.name
    user_surname = app.profile.surname
    print(f'{len(user_name)} characters make up your name and \n{len(user_surname)} characters make up your surname')


def number_of_vowels():
    user_name = app.profile.name.lower()
    user_surname = app.profile.surname.lower()

    vowels_count = {
        'name': {},
        'surname': {}
    }
    for vowels in "aeiou":
        count_name = user_name.count(vowels)
        count_surname = user_surname.count(vowels)
        vowels_count['name'][vowels] = count_name
        vowels_count['surname'][vowels] = count_surname

    print(VOWELS_NAME.format(*vowels_count['name'].values()))
    print(VOWELS_SURNAME.format(*vowels_count['surname'].values()))


def ascii_number():
    sum_ascii = sum(map(ord, app.profile.name))
    print(
        f'The number resulting from adding the ASCII numbers that make up your name and surname is: {sum_ascii}')


def get_number_input(label):
    try:
        value = float(input(f'{label}: \n'))
        return value
    except ValueError:
        print('Please insert a valid number. The value cannot contain commas, spaces, or characters.')
        # Repeat until correct value
        return get_number_input(label)

def profit_of_order():
    op_value = get_number_input('Please enter the operation value')
    perc_profits = get_number_input('Please enter the percentage of profits')

    profit = round(op_value * (perc_profits / 100), 2)
    print(f'The profit (or losses) that you have obtained is {profit}\n')


calculation_options = {
    'l': length_name,
    'n': number_of_vowels,
    'a': ascii_number,
    'p': profit_of_order
}


def calculation_module():
    while True:
        calculation_answer = input(f'\n{TASK} {CALCULATION_MENU}')
        # 'e' option exits calculation module
        if calculation_answer == 'e':
            break

        try:
            calculation_options[calculation_answer]()
        except KeyError:
            print(OPTIONS_ERROR)