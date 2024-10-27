def get_multiplied_digits(number):
    """Пример использования рекурсии. Функция возвращает произведение чисел, составляющих число"""
    str_number = str(number)
    while str_number[-1] == '0':  #  Проверка на наличия нуля последним символом
        str_number = str_number[:-1]
    if len(str_number) <= 1:
        return int(str_number)  # Если длина строки с числом не больше 1, возвращаем это число
    else:
        first = int(str_number[0])  # Получаем первую цифру числа
        rest_of_number = int(str_number[1:]) # Отрезаем первую цифру от числа
        result = get_multiplied_digits(rest_of_number) # Вычисляем произведение оставшихся цифр
        return first * result  # Возвращаем результат умножения первой цифры на произведение остальных цифр

# Пример использования функции
num1 = 42000
num2 = 1001030
num3 = 2203400

res1 = get_multiplied_digits(num1)
res2 = get_multiplied_digits(num2)
res3 = get_multiplied_digits(num3)
print("Произведение цифр числа", num1, "равно", res1)
print("Произведение цифр числа", num2, "равно", res2)
print("Произведение цифр числа", num3, "равно", res3)
