#Vehicle и Sedan
"""    Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)"""
from itertools import count


class Vehicle:
    COLOR_VARIANTS = ('black', 'green', 'yellow', 'blue', 'red') # private

    def __init__(self, owner: str, model: str, color: str, engine_power: int) -> None:
        self._owner = owner # private
        self.__model = model # protected
        self.__engine_power = engine_power # protected
        self.__color = color # protected

    @property
    def owner(self) -> None:
        return print(f'Владелец: {self._owner}')

    @owner.setter
    def owner(self, value: str) -> None:
        self._owner = value

    @property
    def get_model(self) -> None:
        return print(f'Модель: {self.__model}')

    @property
    def get_engine_power(self) -> None:
        return print(f'Мощность двигателя: {self.__engine_power}')

    @property
    def get_color(self) -> None:
        return print(f'Цвет: {self.__color}')

    def set_color(self, new_color: str) -> str | None:
        for color in self.COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                return self.__color
            else:
                return print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self) -> None:
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self._owner}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner: str, model: str, engine_power: int, color: str) -> None:
        self._owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def print_info(self) -> None:
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self._owner}')
        print(f'Количество пассажиров: {self.__PASSENGERS_LIMIT}')

if __name__ == '__main__':
    """car = Vehicle('Tormozzz','Oka', 45, 'blue')
    car.get_color
    car.change_color('grEEn')
    car.get_color
    car.print_info()
    #car.COLOR_VARIANTS.append('orange')"""

    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
