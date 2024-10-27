def get_multiplied_digits(number):
    """Пример использования рекурсии. Функция возвращает произведение чисел, составляющих число"""
    str_number = str(number)
    if len(str_number) <= 1:
        return int(str_number)  # Если длина строки с числом не больше 1, возвращаем это число
    else:
        first = int(str_number[0])  # Получаем первую цифру числа
        rest_of_number = int(str_number[1:]) # Отрезаем первую цифру от числа
        result = get_multiplied_digits(rest_of_number) # Вычисляем произведение оставшихся цифр
        return first * result  # Возвращаем результат умножения первой цифры на произведение остальных цифр

# Пример использования функции
num = 31124578434
res = get_multiplied_digits(num)
print("Произведение цифр числа", num, "равно", res)
