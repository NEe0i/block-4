def get_year_name(n):
    # Списки животных и цветов
    animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея",
               "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
    colors = ["Зеленый", "Красный", "Желтый", "Белый", "Черный"]

    # Находим номер года в 60-летнем цикле
    year_in_cycle = (n - 1984) % 60

    # Определяем индекс животного и цвета
    animal_index = year_in_cycle % 12      # 12 животных
    color_index = (year_in_cycle // 12) % 5  # 5 цветов

    # Получаем название года
    year_name = f"{animals[animal_index]}, {colors[color_index]}"
    return year_name


# Случай а: значение n = 1984
n1 = 1984
print(f"{n1}: {get_year_name(n1)}")

# Случай б: значение n может быть любым натуральным числом
n2 = int(input("Введите год нашей эры: "))
print(f"{n2}: {get_year_name(n2)}")
