a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
d = int(input("Введите число: "))
num1 = 0
num2 = 0
num3 = 0
num4 = 0
if a % 3 == 0:
    num1 = a
if b % 3 == 0:
    num2 = b
if c % 3 == 0:
    num3 = c
if d % 3 == 0:
    num4 = d
print(f"Результат равен {num1 + num2 + num3 + num4}")
