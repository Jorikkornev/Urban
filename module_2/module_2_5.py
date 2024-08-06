#  Задача "Матрица воплоти"

"""
Напишите функцию get_matrix с тремя параметрами n, m и value,
которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
заполненную значениями value и возвращать эту матрицу в качестве результата работы.
"""


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


res1 = get_matrix(2, 2, 10)
res2 = get_matrix(3, 5, 42)
res3 = get_matrix(4, 2, 13)
print(res1, res2, res3, sep='\n')
