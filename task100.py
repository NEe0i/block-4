number1 = int(input("Введите число: "))
number2 = int(input("Введите число: "))
number3 = int(input("Введите число: "))

if number1 >= number2 and number1 >= number3:
    print(number2 * number3)
elif number2 >= number1 and number2 >= number3:
    print(number1 * number3)
else:
    print(number1 * number2)
