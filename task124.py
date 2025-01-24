def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"

    sides = sorted([a, b, c])
    x, y, z = sides

    if x ** 2 + y ** 2 == z**2:
        angle_type = "Прямоугольный"
    elif x ** 2 + y ** 2 > z**2:
        angle_type = "Остроугольный"
    else:
        angle_type = "Тупоугольный"

    if a == b == c:
        shape_type = "Равносторонний"
    elif a == b or a == c or b == c:
        shape_type = "Равнобедренный"
    else:
        shape_type = "Разносторонний"

    return angle_type, shape_type


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

result = triangle_type(a, b, c)
if isinstance(result, tuple):
    print(f"Вид треугольника: {result[0]}")
    print(f"Особенности треугольника: {result[1]}")
else:
    print(result)
