from math import sqrt

num1 = int(input("Введите число "))
num2 = int(input("Введите число "))

num22 = sqrt(num2)

if num22 < num1:
    num2 = num2 * 5
    print(num2)
