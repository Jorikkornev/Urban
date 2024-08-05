#  Задание "Средний балл":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#  Решение без цикла
#  Вычисление среднего арифметического
average = []
'''
average += [sum(grades[0]) / len(grades[0])]
average += [sum(grades[1]) / len(grades[1])]
average += [sum(grades[2]) / len(grades[2])]
average += [sum(grades[3]) / len(grades[3])]
average += [sum(grades[4]) / len(grades[4])]
'''
#  Решение с циклом
for item in grades:
    average += [sum(item) / len(item)]
print(average, type(students))

#  Перевод в список с сортировкой
students_list = list(students)
students_dict = dict(zip(students_list, average))
sort = sorted(students_dict.items())
print(sort)
