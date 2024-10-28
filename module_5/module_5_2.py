#  5_2 Домашняя работа по уроку "Специальные методы классов
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

if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))