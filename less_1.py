# print() - вывод данных в консоль
print("Hello World")

# type() - тип переменной
print('abc', type('abc'))
print(5, type(5))
print(5 / 2, type(5 / 2))
print(5 // 2, type(5 // 2))
print(2 ** 5, type(2 ** 5))
print("1" + '1', type("1" + '1'))  # Конкатинация
print(2 > 5, type(2 > 5))  # Boolean
print(type(int('5')))  # Преобразование типов

# Homework

# 1st program

print(9 ** 0.5 * 5)

# 2st program

print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program

print((1234 % 1000 // 10) + (5678 % 1000 // 10))

# 4th program

# Сравнение целой части первого числа со второй частью дробного

print(int(54.39) == int(37.54 * 100 % 100) or int(37.54 * 100 % 100) == int(54.39))

# Вариант с переменными

x, y = 10.39, 37.1
print(int(x) == int(y * 100 % 100) or int(y * 100 % 100) == int(x))
