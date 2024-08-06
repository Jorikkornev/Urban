#  Задача "Все ли равны?"

# Для сокращения ввода данных использую список
nums = input("Введите три целых числа через пробел: ")
nums = nums.split()
#  Проверка на количество чисел
while len(nums) < 3:
    # Чисел/Число
    if len(nums) == 1:
        word = "числа"
    else:
        word = "число"
    print(f"Введите еще {3 - len(nums)} {word} через пробел")
    dop_nums = input()
    dop_nums = dop_nums.split()
    nums.extend(dop_nums)
#  Если больше трёх - берутся первые три числа
if len(nums) > 3:
    nums = nums[0:3]
# Проверка введённых данных на соответсвие типу
i: int = 0
while i < len(nums):
    if nums[i].isnumeric():
        nums[i] = int(nums[i])
        i += 1
    else:
        # Повторный ввод, если не число
        print(f"{nums[i]} - не число, повторите ввод")
        nums[i] = input("Введите число: ")
# Создание переменных из массива
first, second, third = nums

# Реализация условия задания
if first == second == third:
    print("Все числа равны, ", 3)
elif first == second or second == third or third == first:
    print("Два числа равны, ", 2)
else:
    print("Числа не равны, ", 0)
