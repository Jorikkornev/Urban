from traceback import print_exception


def print_params(a = 1, b = 'строка', c = True):
    print("a:", a, type(a))
    print("b:", b, type(b))
    print("c:", c, type(c))
values_list_3 = [11, 'eleven', False]
values_list_2 = [11, 'eleven']
values_dict_3 = {'a' : 11, 'b' : 'eleven', 'c' : False}
values_dict_2 = {'a' : 11, 'b' : 'eleven'}
# Вызов функции без аргументов
print_params()

# Вызов функции с одним аргументом
print_params(b = 25)

# Вызов функции с двумя аргументами
print_params(c = [1,2,3])

print('Test1 :')

print_params(c = [1,2,3])
print_params(b = 25)


print_params(*values_list_3)
print_params(**values_dict_3)

print('Test2 :')
print_params(*values_list_2)
print_params(**values_dict_2)

