number = int(input("Введите двузначное число: "))
a = int(input("Введите цифру для проверки: "))
number_str = str(number)

if '3' in number_str:
    print("Цифра 3 входит в число.")
else:
    print("Цифра 3 не входит в число.")

if str(a) in number_str:
    print(f"Цифра {a} входит в число.")
else:
    print(f"Цифра {a} не входит в число.")
