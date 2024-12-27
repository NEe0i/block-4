from math import sin

x = int(input("введите число: "))

if x > 0:
    y = (sin(x)) ** 2
    print(y)
else:
    y = 1 - 2 * ((sin(x)) ** 2)
    print(y)
