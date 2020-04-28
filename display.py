def print_program_menu(menu_commands):
    for option in menu_commands:
        print(str(menu_commands.index(option)) + " " + option)


def print_user_info(filename):
    '''ID,Name, Weight, Height, BMI, Restrictions'''
    ID_INDEX = 0
    NAME_INDEX = 1
    WEIGHT_INDEX = 2
    HEIGHT_INDEX = 3
    BMI_INDEX = 4

    for row in filename:
        print('User info: {} with BMI {}'.format(row[ID_INDEX], row[BMI_INDEX]))

def display_numbered_list(data):
    for item in data:
        print(str(data.index(item))+' '+item)

def print_result(message):
    vertical_spacing = 2
    print(vertical_spacing * '\n' + message)
