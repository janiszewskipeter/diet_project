import display
import diets
import file_handling


def main():
    while True:
        initialize_program_menu()
        try:
            user_menu_input()
        except KeyError:
            print("Key Error -  PLease ")


def get_user_input(question):
    input_from_keyboard = input(question)
    return input_from_keyboard


def initialize_program_menu():
    NUMBER_OF_STARS_DECOR = 25
    DECOR_LINE = "*" * NUMBER_OF_STARS_DECOR
    HEADER = "Diet & BMI calculator"
    display.print_result(DECOR_LINE)
    display.print_result(HEADER)
    display.print_result(DECOR_LINE)
    options = [
                "User input","BMI calc", 
                "Diet proposal", "Diet restrictions",
                "Workout", "Quit"]
    display.print_program_menu(options)


def user_menu_input():
    FIRST_MENU_QUESTION = "What do You want to do?"
    BMI_HEIGHT = "Type Your height"
    BMI_WEIGHT = "Type Your weight"
    BMI_AGE = "Type Your Age"
    BMI_RESOULT = "Your BMI is: " 
    USER_INFO = '0'
    BMI_CALC = '1'
    DIET_PROPOSAL = '2'
    DIET_RESTRICTIONS = '3'
    WORKOUT_PROPOSAL = '4'
    END_PRIOGRAM = '5'

    data = file_handling.import_data(filename='user_profile.txt')
    user_input = get_user_input(FIRST_MENU_QUESTION)

    if user_input == USER_INFO:
        display.print_user_info(data)
    elif user_input == BMI_CALC:
        height = get_user_input(BMI_HEIGHT)
        weight = get_user_input(BMI_WEIGHT)
        age = get_user_input(BMI_AGE)
        bmi_raport = diets.get_bmi_report(height, weight, age)
        display.print_result(BMI_RESOULT + bmi_raport)
    elif user_input == DIET_PROPOSAL:
        pass
    elif user_input == DIET_RESTRICTIONS:
        pass
    elif user_input == WORKOUT_PROPOSAL:
        pass
    elif user_input == END_PRIOGRAM:
        pass
    else:
        raise KeyError


main()
