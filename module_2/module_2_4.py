#  Задача "Всё не так уж просто":

"""
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
"""

#  Первый вариант - в две итерации (Вспомнил задачу по поиску чисел Фибоначчи)
#  Первое простое число - 2, добавил для исключения из поиска
primes = [2, ]
not_primes = []
numbers = list(range(1, 33))

#  Заполнение простыми числами
#  С помощью шага 2 отбрасываются чётные числа
for i in range(3, 33, 2):
    #  Делится на 3 или 5
    if (i > 3 and i % 3 == 0) or (i > 5 and i % 5 == 0):
        continue
    else:
        primes.append(i)

# Заполнение составных чисел

for i in range(4, 33):
    if i in primes:
        continue
    else:
        not_primes.append(i)
print("Простые числа: ", primes)
print("Составные числа: ", not_primes)
print("Массив чисел: ", numbers)

#  Решение по задаче

primes_1 = []
not_primes_1 = []

for i in numbers:
    if i == 1:
        continue
    else:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes_1.append(i)
        else:
            not_primes_1.append(i)

print("Решение по задаче")
print("Простые числа: ", primes_1)
print("Составные числа: ", not_primes_1)
print("Массив чисел: ", numbers)
