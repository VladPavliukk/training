
name = input("Добрий день, як вас звати? ")
print(f"Привіт, козаче, давно ми не бачили {name}")

age = int(input("Скільки вам років? "))
height = float(input("Бро, а ти високий? Як сильно? "))
weight = float(input("Скільки можеш пожати в качалці? Давай спочатку свою вагу "))




if age < 10 or height <= 0 or height >= 3 or weight <= 0 or weight > 500:
    print("Бро, може почнеш писати нормально?")

else:
    bmi = round(weight/height ** 2, 2)
    print(f"Твій індекс маси тіла = {bmi}")

    if bmi < 18.5:
        description = "шото маловато"
    elif bmi < 25:
        description = "ооо, оце норм"
    elif bmi < 30:
        description = "бро, нада сушка"
    else:
        description = "тут вже сушка не поможе, нада худать, бро, ожирєніє"

    print(f"Ти относишся до людей {name} з {description}")