num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))

if abs(num1) > abs(num2):
    num1 /= 2
    
print(F"Результат равен {num1}")
