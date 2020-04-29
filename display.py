def print_program_menu(menu_commands):
    for option in menu_commands:
        print(str(menu_commands.index(option)) + " " + option)
    print()


def print_user_info(user_info):
    '''ID,Name, Weight, Height, BMI, Restrictions'''
    # ID_INDEX = 0
    # NAME_INDEX = 1
    # WEIGHT_INDEX = 2
    # HEIGHT_INDEX = 3
    # BMI_INDEX = 4

    # for row in filename:
    #     print('User info: {} with BMI {}'.format(row[ID_INDEX], row[BMI_INDEX]))

    headers = ['ID','Name', 'Weight', 'Height', 'BMI', 'Restrictions']
    print()
    for item in user_info:
        longest_cell = max([len(i) for i in headers])
        header_len = len(headers[user_info.index(item)])
        print((headers[user_info.index(item)])+(longest_cell - header_len)*' '+" | "+item)
    print()

def display_numbered_list(data):
    for item in data:
        print(str(data.index(item))+' '+item)
    print()

def print_result(message):
    vertical_spacing = 2
    print(vertical_spacing * '\n' + message)
    print()

def print_tab_result(result):
    for i in result:
        print(' | '.join(i))
    print()
