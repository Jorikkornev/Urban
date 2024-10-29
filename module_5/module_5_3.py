# 5_3 Домашняя работа по уроку "Перегрузка операторов"
# Просится функция для генерации подобного кода...
class House:
    def __init__(self, house_addr, number_of_floors, ):
        self.house_addr = house_addr
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            return print("Такого этажа не существует")
        else:
            c = 1
            while c <= new_floor:
                print(c)
                c += 1
        return

    def __len__(self):  # Возвращает количество этажей в len()
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.house_addr}, кол-во этажей: {self.number_of_floors}"


    def __lt__(self, other):  # <
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            return f"У {other.house_addr}, не корректное количество кол-во этажей: {other.number_of_floors}"

    def __le__(self, other):  # <=
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            return f"У {other.house_addr}, не корректное количество кол-во этажей: {other.number_of_floors}"

    def __gt__(self, other):  #  >
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            return f"У {other.house_addr}, не корректное количество кол-во этажей: {other.number_of_floors}"

    def __ge__(self, other):  #  >=
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            return f"У {other.house_addr}, не корректное количество кол-во этажей: {other.number_of_floors}"

    def __ne__(self, other):  #  !=
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            return f"У {other.house_addr}, не корректное количество кол-во этажей: {other.number_of_floors}"

    def __eq__(self, other):  #  ==
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        else:
            return f"У {other.house_addr}, не корректное количество кол-во этажей: {other.number_of_floors}"

    def __add__(self, value):  #  self = self + val
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return f"Не корректное значение, {value}"

    def __iadd__(self, value):  #  self += val
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return f"Не корректное значение, {value}"

    def __radd__(self, value):  #  self = val + self
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return f"Не корректное значение, {value}"


if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__