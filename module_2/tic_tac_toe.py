# Крестики нолики
import random
from typing import Any


# TODO
# TODO 1. Написать функцию определения победителя, которая прогоняет цикл
#    и считает по условиям:
#    [i1j1,i1j2,i1j3] - строка, [i2j1,i2j1,i3j1] - ряд, [i1j1,i2j2,i3j3] - диагональ +
# TODO 2. Проверяет пустое ли поле, если нет - continue
# TODO 3. Учесть переменную ходов для ничьи - step_count = 9 +
# TODO 4. Сделать функцию - чей первый ход +
# TODO 5. Сделать игру с ПК - ? *
# TODO 6. Функцию, отрисовывающию поле +
# TODO 7. Функцию для проверки двух введённых в массив чисел, с разбивкой на строку-ряд +
# TODO 8. Сделать рефакторинг кода, функции проверки -> bool, операции с файлами - в основном теле игры,
#  возможно - полностью оперировать со строками?
# TODO 9. Описать код, потренироваться в тестировании
# Функции
def def_winner(test_game_field: list[Any], marker: str) -> None | str:
    """Функция определяет победителя, переводя числовое игровое поле в текстовое"""
    str_f = ''
    marker_3 = marker * 3
    for lev_1 in test_game_field:
        for lev_2 in lev_1:
            str_f += str(lev_2)
    diag_1 = str_f[0::4]
    diag_2 = str_f[2:8:2]
    print('d_1 : ', diag_1, 'd_2 : ', diag_2, 'mid_line : ', str_f.find(marker_3, 3, 7))
    if str_f.startswith(marker_3) > 0 \
            or str_f.endswith(marker_3) > 0 \
            or str_f.find(marker_3, 3, 6) > 0:
        #  print('Win for Line', 'str_f: ', str_f, 'marker: ', marker_3)
        return f"{marker} Win!"
    if diag_1 == marker_3 or diag_2 == marker_3:
        # print('Win for Diagonal', 'd_1 : ', diag_1, 'd_1', diag_2, )
        return f"{marker} Win!"
    else:
        return


# TODO 4
def first_player(name_1: str, name_2: str) -> tuple[str, str]:
    """Функция, определяющего игрока, который ходит Х"""
    first = int(random.randint(1, 2))
    if first == 1:
        print(f"X ходит игрок {name_1}")
        return name_1, name_2
    else:
        print(f"X ходит игрок {name_2}")
        return name_2, name_1


#  TODO 7
def check_data(sings: str) -> list[int] | None:
    """Функция, проверяющая корректность введённых данных"""
    nums = sings.split()
    if len(nums) != 2:  # Проверка на 2 числа
        print(f"Вы ввели не верное количество символов и пропускаете ход", len(sings))
        return
    else:
        x, y = nums
    print(x, y, x.isnumeric(), y.isnumeric())
    # Функции проверки по True, "белый список", всё, что не подходит под указанные условия - False
    if x.isnumeric() is True and y.isnumeric() is True:
        x = int(x)
        y = int(y)
    else:
        print(f"Вы ввели не корректное значение и пропускаете ход X: {x}, Y: {y}")
        return
    if (0 < x < 4) and (0 < y < 4):  # Проверка для соответствия индексов игрового поля 1-3 индексам списка
        # game_field 0-2
        if x != 0:
            x = x - 1
        if y != 0:
            y = y - 1
        sings = [x, y]
        print('Tested int!', x, y)
        return sings
    else:
        print(f"Вы ввели не корректное значение и пропускаете ход X: {x}, Y: {y}")
        return
    #


def check_game_position(test_game_field: list[Any], x: int, y: int) -> bool:
    """Функция проверки занята или нет позиция по указанным координатам"""
    if test_game_field[x][y] != '*':
        print("Вы ввели не пустое поле и пропускаете ход")
        return False
    else:
        return True


# Вспомогательные функции для проверки значений

# Проверка введённых данных на соответсвие типу


# Start Игровое поле
def print_field(field: list):
    """Функция, отрисовывающая игровое поле после хода"""
    for s in range(3):
        print(*field[s], sep="\t")


game_field = []  # Создание и заполнение * игрового поля
for k in range(3):
    game_field.append([])  # Создается три списка
    for j in range(3):
        game_field[k].append("*")

# End Игровое поле


# Welcome
print("Добро пожаловать в игру!")
print_field(game_field)  # Отрисовка чистого поля
player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")
player_1, player_2 = first_player(player_1, player_2)  # Кто ходит первым, Х
print(player_1, player_2)
for i in range(9):
    #  Крестик или нолик - ?
    if i % 2 == 0:
        sing = "X"
        print(f"Крестик ходит, {player_1}, твой ход")
    else:
        sing = "0"
        print(f"Нолик ходит, {player_2}, твой ход")
    pos = input("Введите позицию строки и ряда через пробел: ")
    checked_nums = check_data(pos)
    if type(checked_nums) is list and len(checked_nums) == 2:
        pos_x = checked_nums[0]
        pos_y = checked_nums[1]
        print(pos_x, pos_y, type(pos_x), type(pos_y))
    else:
        print_field(game_field)
        continue
    checked_pos = check_game_position(game_field, pos_x, pos_y)
    if checked_pos:
        game_field[pos_x][pos_y] = sing
        print_field(game_field)
    else:
        print_field(game_field)
        continue
    winner = def_winner(game_field, sing)
    print("i : ", i)
    if bool(winner):
        print(winner)
        break
    elif i == 8 and not bool(winner):
        print(f"End of a game {player_1}, {player_2} you are Luser's")
    #  TODO
