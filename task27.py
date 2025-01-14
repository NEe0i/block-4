num = int(input("Введите трехзначное число: "))

num_str = str(num)

if num_str == num_str[::-1]:
    print("Число является палиндромом.")
else:
    print("Число не является палиндромом.")