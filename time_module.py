# Time Module

from datetime import datetime
import app
from strings import TIME_MENU, TASK, OPTIONS_ERROR


def calculate_days():
    date = datetime.now().date()
    date1 = datetime(date.year, app.profile.birthday.month,
                     app.profile.birthday.day).date()
    date2 = datetime(date.year + 1, app.profile.birthday.month,
                     app.profile.birthday.day).date()
    return ((date1 if date1 > date else date2) - date).days


def days_until_birthday():
    print(f'There are {calculate_days()} days until your birthday \n')


def view_time():
    print(
        f'The current time is (H:M:S) {datetime.now().strftime("%H:%M:%S")}\n')


time_options = {
    'v': view_time,
    'd': days_until_birthday
    }


def time_module():
    while True:    
        time_answer = input(f'\n{TASK} {TIME_MENU}')
        print("\n")
        # 'e' option exits time module
        if time_answer == 'e':
            break

        try:
            time_options[time_answer]()
        except KeyError:
            print(OPTIONS_ERROR)