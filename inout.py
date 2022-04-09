import app


def load(file_name):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        values = [line.split(': ')[1] for line in lines]
        if values:
            app.profile.set_all_fields(*values)


def save(file_name):
    with open(file_name, 'w') as file:
        file.write(app.profile.get_profile_information())