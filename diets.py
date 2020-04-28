def get_bmi_report(height, weight, age):
    height = int(height)/100
    weight = int(weight)
    age = int(age)
    bmi_report = str(weight / (height * height))
    return bmi_report  