
# Рекурсивная функция для сглаживания списка
def flatten(lst):
    result = []
    for item in lst:
        #  Для уменьшения количества рекурсий выполняется проверка пустых значений
        if isinstance(item, bool) and item == False or bool(item) == False:  #
            continue
        elif isinstance(item, (list, tuple, set, dict)):
            if isinstance(item, dict):  #  Если словарь - перевести в список
                item = list(item.items())
            item = list(item)
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def summ_list(*args, **kwargs):
    summ = 0
    all_list = flatten(args)  # Заполнение массива данными
    for item in all_list:
        if isinstance(item, str) and item.isnumeric(): #  Если строка переводится в число - суммируем
            summ += int(item)
        elif isinstance(item, (int, float)):  # Если число - суммируем
            summ += item
        else:
            summ += len(item)  # Если строка - суммируем длину строки
    return summ

nestedlist = [
    11, [1, 2, 3], 0, False, True,
    {'a': 4, 'b': 5, 'test' : 'tested!'},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", 20, {13, 17},
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
t = flatten(nestedlist)
print(t)
s = summ_list(nestedlist)
print(s)