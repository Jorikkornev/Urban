import random
import unittest


num_first = random.randint(3, 21)  #  Первое число - случайное число из диапазона от 3 до 20


def test_second(first: int) -> str:
    """Функция подбора пар чисел, кратных первому числу, согласно условию num_first % (i + k) == 0"""
    second = ''
    for i in range(1, first):  # Первый, внешний цикл от 1 до first
        for k in range(i + 1, first):  # Второй, внутренний цикл от i+1 до first
            pairs_sum = i + k
            if first % pairs_sum == 0:
                second += str(i) + str(k)
    return second


num_second = int(test_second(num_first))
print(f"Число на первом камне : {num_first}, код для второго камня: {num_second}")


class TestEqual(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_eq_res(self):
        result = test_second(18)
        self.assertEqual(result, '12151811724272163631545414513612711810')

# TODO """Сделать контрольный словарь для проверки без тестов из задания
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911
