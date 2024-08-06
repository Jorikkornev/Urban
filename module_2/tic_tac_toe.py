# Крестики нолики
import random
from random import randint


# TODO
# TODO 1. Написать функцию определения победителя, которая прогоняет цикл
#    и считает по условиям:
#    [i1j1,i1j2,i1j3] - строка, [i2j1,i2j1,i3j1] - ряд, [i1j1,i2j2,i3j3] - диагональ
# TODO 2. Проверяет пустое ли поле, если нет - continue
# TODO 3. Учесть переменную ходов для ничьи - step_count = 9
# TODO 4. Сделать функцию - чей первый ход
# TODO 5. Сделать игру с ПК - ?
# TODO 6. Функцию, отрисовывающию поле
# TODO 7. Функцию для ввода двух чисел, с разбивкой на строку-ряд

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
def print_field():
    for s in range(3):
        print(*game_field[s], sep="\t")


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
print_field()
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
    sing_x = input()
