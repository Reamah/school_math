def calculate_area(length, width):
    """Функция для вычисления площади прямоугольника"""
    area = length * width
    return area

# Запрос пользовательского ввода
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

# Вызов функции и вывод результата
result = calculate_area(length, width)
print("Площадь прямоугольника:", result)
