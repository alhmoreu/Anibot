# Profile Module
from Profile import UnsuitableValue
from datetime import datetime
import app
from inout import save
from strings import PROFILE_MENU, TASK, OPTIONS_ERROR, UPDATE_PROFILE_STR0, DOWNLOAD_INFORMATION_STR, UPDATE_PROFILE_STR
from print import print_error, print_hint

def download_information():
    name_folder = input(DOWNLOAD_INFORMATION_STR)
    file_name = f'./{name_folder}.txt'

    save(file_name)


def view_profile():
    print(app.profile.get_profile_information())


def check_valid_field(value):
    isEmpty = len(value) == 0
    isNumber = False
    
    try:
        float(value)
        isNumber = True
    except ValueError:
        pass           

    return not isEmpty and not isNumber


def verify_birthday_format(birthday):
    try:
        return bool(datetime.strptime(birthday, '%Y-%m-%d').date())
    except ValueError:
        return False


profile_fields = [
     {
         "input_text": "'Name' length must be a string and greater than 0:",
         "is_valid": check_valid_field,
         "field": 'Name'
 
     },
     {
         "input_text": "'Surname' length must be a string and greater than 0:  \n",
         "is_valid": check_valid_field,
         "field": 'Surname'
 
     },
     {
         "input_text": "'Gender' enter a 'M' if masculine or a 'F' if feminine \n",
         "is_valid": lambda v: v in ['M', 'F'],
         "field": 'Gender'
     },
     {
         "input_text": "'Age' must be an integer:  \n",
         "is_valid": lambda v: v.isnumeric(),
         "field": 'Age'
     },
     {
         "input_text": "'Birthday' must have format yyyy-mm-dd:  \n",
         "is_valid": verify_birthday_format,
         "field": 'Birthday'
     }
 ]

 
def update_profile():
    print('This is your profile information \n')
    actual_values = [*app.profile.__dict__.values()]
    print(app.profile.get_profile_information())
    print(UPDATE_PROFILE_STR)

    field_values = []

    for i, field_obj in enumerate(profile_fields):
        prev_value = actual_values[i]

        while True:
            print(UPDATE_PROFILE_STR0.format(field_obj["field"]))
            print_hint(field_obj["input_text"])

            new_value = input()

            # Use previous value
            if not new_value:
                if not prev_value:
                    print_error('You cannot skip this field as there was not a previous value')
                    continue

                break

            valid_new_value = field_obj["is_valid"](new_value)
            if valid_new_value:
                break

        field_values.append(new_value or prev_value)
    
    app.profile.set_all_fields(*field_values)
    save(app.SAVE_FILENAME)


profile_options = {
    'u': update_profile,
    'v': view_profile,
    'd': download_information,
}


def profile_module():
    while True:
        profile_answer = input(f'\n{TASK} {PROFILE_MENU}')
        # 'e' option exits profile module
        if profile_answer == 'e':
            break

        try:
            profile_options[profile_answer]()
        except KeyError:
            print(OPTIONS_ERROR)