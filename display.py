def print_program_menu(menu_commands):
    for option in menu_commands:
        print(str(menu_commands.index(option))+ " " + option)


def print_user_info():
    pass


def print_result(message):
    vertical_spacing = 2
    print(vertical_spacing * '\n' + message)