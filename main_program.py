import display
import diets
import file_handling
import sys
import os

def get_user_data_for_login(login, users, USER):
    logins = [user[USER] for user in users if user[USER] == login]
    user_index = logins.index(login)

    return user_index


def get_user_input(question):
    input_from_keyboard = input(question)
    return input_from_keyboard

def print_splash():
    NUMBER_OF_STARS_DECOR = 25
    DECOR_LINE = "*" * NUMBER_OF_STARS_DECOR
    HEADER = "Diet & BMI calculator"
    display.print_result(DECOR_LINE)
    display.print_result(HEADER)
    display.print_result(DECOR_LINE)

def initialize_program_menu():
    options = [
                "Users Info","BMI calc", 
                "Diet proposal", "Diet restrictions",
                "Workout", "Quit"]
    display.print_program_menu(options)


# def user_menu_input():
   

def login():
    login = get_user_input("Enter you login:\n")
    password = get_user_input("Enter password:\n")

    return login

def main():
    os.system('clear')
    USER = 1
    RESTRICTION = 5
    FIRST_MENU_QUESTION = "What do You want to do?"
    BMI_HEIGHT = "Type Your height"
    BMI_WEIGHT = "Type Your weight"
    BMI_AGE = "Type Your Age"
    HEIGHT = 3
    WEIGHT = 2
    BMI = 4
    BMI_RESOULT = "Your BMI is: " 
    USER_INFO = '0'
    BMI_CALC = '1'
    DIET_PROPOSAL = '2'
    DIET_RESTRICTIONS = '3'
    WORKOUT_PROPOSAL = '4'
    END_PRIOGRAM = '5'
    filename = 'user_profile.txt'
    data = file_handling.import_data(filename='user_profile.txt')   
    diets_list = file_handling.import_data(filename='diets.txt')    
    restriction_submenu = ['Vegan','Vegetarian','Low Fat']
    user_login = login()
    user_index = get_user_data_for_login(user_login, data, USER)
    is_running = True

    print_splash()
    
    while is_running:
        initialize_program_menu()
        try:
            user_input = get_user_input(FIRST_MENU_QUESTION)
        except KeyError:
            print("Key Error -  PLease ")
        if user_input == USER_INFO:
            os.system('clear')
            display.print_user_info(data[user_index])
        elif user_input == BMI_CALC:
            os.system('clear')
            height = get_user_input(BMI_HEIGHT)
            weight = get_user_input(BMI_WEIGHT)
            age = get_user_input(BMI_AGE)
            data[user_index][HEIGHT] = height
            data[user_index][WEIGHT] = weight
            bmi_raport = diets.get_bmi_report(height, weight, age)
            display.print_result(BMI_RESOULT + bmi_raport)
            data[user_index][BMI] = bmi_raport 
        elif user_input == DIET_PROPOSAL:
            restriction = data[user_index][RESTRICTION]
            diet = diets.get_diet(diets_list, data, restriction)
            display.print_tab_result(diet)
        elif user_input == DIET_RESTRICTIONS:
            display.display_numbered_list(restriction_submenu)
            restriction = get_user_input("Enter your restriction:\n")
            if restriction == '0':
                data[user_index][RESTRICTION] = 'Vegan'
            elif restriction == '1':
                data[user_index][RESTRICTION] = 'Vegetarian'
            elif restriction == '2':
                data[user_index][RESTRICTION] = 'LowFat'
            else:
                raise KeyError
        elif user_input == WORKOUT_PROPOSAL:
            pass
        elif user_input == END_PRIOGRAM:
            file_handling.data_export(filename, data)
            is_running = False
        else:
            raise KeyError 
        


main()
