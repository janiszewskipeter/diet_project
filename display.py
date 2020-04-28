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

    print('User info: {} with BMI {}'.format(filename[NAME_INDEX], filename[BMI_INDEX]))


def print_result(message):
    vertical_spacing = 2
    print(vertical_spacing * '\n' + message)
