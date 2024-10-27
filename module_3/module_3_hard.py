

def flatten(lst):
    """Рекурсивная функция для сглаживания списка"""
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
    """Функция получает список и суммирует его значения согласно условиям"""
    summ = 0
    all_list = flatten(args)  # Заполнение списка данными
    for item in all_list:
        if isinstance(item, str) and item.isnumeric(): #  Если строка переводится в число - суммируем
            summ += int(item)
        elif isinstance(item, (int, float)):  # Если число - суммируем
            summ += item
        else:
            summ += len(item)  # Если строка - суммируем длину строки
    return summ

# Объект из примера изменён
nestedlist = [
    11, [1, 2, 3], 0, False, True,
    {'a': 4, 'b': 5, 'test' : 'tested!'},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", 20, {13, 17},
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
data_structure_origin = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

t = flatten(nestedlist)
t1 = flatten(data_structure_origin)
print(t, '\n', t1)
s = summ_list(nestedlist)
s2 = summ_list(data_structure_origin)
print(s, '\n', s2)