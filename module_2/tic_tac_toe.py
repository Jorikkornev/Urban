# Крестики нолики
import random


# TODO
# TODO 1. Написать функцию определения победителя, которая прогоняет цикл
#    и считает по условиям:
#    [i1j1,i1j2,i1j3] - строка, [i2j1,i2j1,i3j1] - ряд, [i1j1,i2j2,i3j3] - диагональ
# TODO 2. Проверяет пустое ли поле, если нет - continue
# TODO 3. Учесть переменную ходов для ничьи - step_count = 9 +
# TODO 4. Сделать функцию - чей первый ход +
# TODO 5. Сделать игру с ПК - ? *
# TODO 6. Функцию, отрисовывающию поле +
# TODO 7. Функцию для проверки двух введённых в массив чисел, с разбивкой на строку-ряд +

# Функции
def def_winner():
    return 0


# TODO 4
def first_player(name_player_1, name_player_2):
    first = int(random.randint(1, 2))
    if first == 1:
        print(f"Первый игрок {name_player_1}")
        return name_player_1, name_player_2
    else:
        print(f"Первый игрок {name_player_2}")
        return name_player_2, name_player_1


# TODO 6
def print_field(field):
    for s in range(3):
        print(*field[s], sep="\t")


#  TODO 7
def check_data(sings):
    #  Переменные
    sings = sings.split()
    is_true = True
    err_text = ""
    input_text = ""
    # Функции проверки
    is_int(sings, is_true, err_text, input_text)


# Вспомогательные функции для проверки значений

# Проверка введённых данных на соответсвие типу
def is_int(sings, is_true, err_text, input_text):
    t = 0
    while t < len(sings):
        if sings[t].isnumeric():
            sings[t] = int(sings[t])
            t += 1
        else:
            # Повторный ввод, если не число
            err_text = f"{sings[t]} - не число, повторите ввод"
            input_text = "Введите число: "
            is_true = False
            return err_text, input_text, is_true, sings[t]
    return is_true


"""
#  Проверка на количество введённых символов

    while len(sings) < 2:
        print(f"Введите номер ряда: ")
        dop_nums = input()
        dop_nums = dop_nums.split()
        sings.extend(dop_nums)
#  Если чисел больше трёх - берутся первые два числа

    if len(sings) > 2:
        sings = sings[0:2]
#  Проверка на попадание в диапазон от 1 до 3

    for s in sings:
        if s < 1 or s > 3:
            s = input("Введите число из диапазона от 1 до 3: ")
            print(sings)
#  Создание переменных из массива
    sing_line, sing_row = sings #TODO вычесть единицу
    return sing_line, sing_row
"""

#  Переменные
game_field = []
#  Заполнение * игрового поля
for k in range(3):
    game_field.append([])
    for j in range(3):
        game_field[k].append("*")
print(game_field)

# Welcome
print("Добро пожаловать в игру!")
print_field(game_field)
player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")
player_1, player_2 = first_player(player_1, player_2)
for i in range(9):
    #  Крестик или нолик - ?
    if i % 2 == 0:
        sing = "X"
        print(f"Крестик ходит, {player_1}, твой ход")
    else:
        sing = "0"
        print(f"Нолик ходит, {player_2}, твой ход")
    pos = input("Введите позицию строки и ряда через пробел: ")
    pos_line, pos_row = check_data(pos)
    #TODO
