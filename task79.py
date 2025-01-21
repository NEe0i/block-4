num1 = float(input("Введите число"))
num2 = float(input("Введите число"))
num3 = float(input("Введите число"))

if num1 < 0:
    num1 = num1 ** 2
if num2 < 0:
    num2 = num2 ** 2
if num3 < 0:
    num3 = num3 ** 2
print(num1, num2, num3)
