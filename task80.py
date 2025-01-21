a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

numbers = [a, b, c]
interval1 = [x for x in numbers if 1.6 < x < 3.8]
interval2 = [x for x in numbers if 0.7 < x < 5.1]
print(f"Числа из первого интервала: {interval1}")
print(f"Числа из второго интервала: {interval2}")
