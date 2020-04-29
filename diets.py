def get_bmi_report(height, weight, age):
    height = int(height)/100
    weight = int(weight)
    age = int(age)
    bmi_report = str(weight // (height * height))

    return bmi_report

def get_diet(diets, data, user_restriction):
    possible_diets = [diet for diet in diets if user_restriction in diet]
    return possible_diets
