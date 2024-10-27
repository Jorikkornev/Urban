from math import inf

def divide(first, second):
    """Функция деления на 0 с результатом бесконечности"""
    if second == 0:
        return inf
    else:
        return first/second