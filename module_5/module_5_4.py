# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, *args, **kwargs):
        self.house_addr, self.number_of_floors = args

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

    def __del__(self):
        print(f" {self.house_addr} снесён, но он останется в истории")

if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)
