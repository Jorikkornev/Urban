from itertools import count


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

if __name__ == "__main__":
    win_street_1 = House('Победы 1', 13)
    win_street_1.go_to(0)
    win_street_1.go_to(10)
    win_street_1.go_to(14)
