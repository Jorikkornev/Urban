#  Списки

#  Кортежи

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True, "String"]
test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True, "String")
print(type(test_list), type(test_tuple))

# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = ([1, 2, 3], 4, 5, 6, 7, 8, 9, 10, True, "String")
print(immutable_var)

#  В кортеже возможно изменение элементов внутри объектов, например - внутри списка
#  Хорошая альтернатива отстутствующим константам
immutable_var[0][2] = 10
#  immutable_var[-1] = "Spring"
#  immutable_var[-2] = False
print(immutable_var)

# Список
mutable_list = list(range(10))
mutable_list.append(True)
print(mutable_list, id(mutable_list))
mutable_list.append("Spring")
print(mutable_list, id(mutable_list))
mutable_list[-1] = "String"
print(mutable_list, id(mutable_list))
