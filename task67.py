k = int(input("Введите число: "))
first_day_of_year = 0
day_of_week = (first_day_of_year + k - 1) % 7
if day_of_week == 5 or day_of_week == 6:
    print("выходной")
else:
    print("рабочий")
