a = int(input("Введите число a: "))
b = int(input("Введите число b: "))


def is_divisor(a, b):
    if b % a == 0:
        return True
    else:
        return False


if is_divisor(a, b):
    print(f"{a} является делителем {b}.")
else:
    print(f"{a} не является делителем {b}.")
