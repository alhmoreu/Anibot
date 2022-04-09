from strings import PROFILE_INFO
from datetime import datetime


class ProfileNotCompleted(Exception):
    pass


class UnsuitableValue(Exception):
    pass

# User information (name, surname, gender, age, birthday)


def is_not_empty(field):
    def is_not_empty_decorator(func):
        def wrapper(*args, **kwargs):
            if args[0].__dict__[field] in [None, '']:
                raise ProfileNotCompleted(
                    f'{func.__name__} is not defined. Please, go to profile module and update the information')

            return func(*args, **kwargs)
        return wrapper
    return is_not_empty_decorator

def check_valid_field(value):
    isEmpty = len(value) == 0
    isNumber = False
    
    try:
        float(value)
        isNumber = True
    except ValueError:
        pass           

    return not isEmpty and not isNumber

class Profile:
    def __init__(self):
        self._name = None
        self._surname = None
        self._gender = None
        self._age = None
        self._birthday = None

    @property
    @is_not_empty("_name")
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    @is_not_empty("_surname")
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname: str):
        self._surname = new_surname

    @property
    @is_not_empty("_gender")
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender: str):
        self._gender = new_gender

    @property
    @is_not_empty("_age")
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: str):
        try:
            age_int = int(new_age)
            self._age = age_int
        except ValueError:
            self._age = input("Please provide a suitable value. Age:  ->")

    @property
    @is_not_empty("_birthday")
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, new_birthday: str):
        try:
            self._birthday = datetime.strptime(new_birthday, '%Y-%m-%d').date()
        except ValueError:
            self._birthday = input(
                "Please provide your birthday with this format 'yyyy-mm-dd': \n")

    def get_profile_information(self):
        return PROFILE_INFO.format(*self.__dict__.values())

    def set_all_fields(self, name, surname, gender, age, birthday):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.birthday = str(birthday)