#Vehicle и Sedan
""" Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)"""

class Vehicle:
    COLOR_VARIANTS = ('black', 'green', 'yellow', 'blue', 'red') # private

    def __init__(self, owner: str, model: str, color: str, engine_power: int) -> None:
        self._owner = owner # private
        self.__model = model # protected
        self.__engine_power = engine_power # protected
        self._color = color # protected

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
        return print(f'Цвет: {self._color}')

    # Вариант наследования с передачей имени класса _Class_name__protected_name
    def set_color(self, new_color: str) -> None:
        for color in self.COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self._color = new_color
                return print(f'Цвет сменен на {new_color}')
            else:
                return print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self) -> None:
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self._color}')
        print(f'Владелец: {self._owner}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner: str, model: str, color: str, engine_power: int) -> None:
        super().__init__(owner, model, color, engine_power)
        self._owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self._color = color

    def print_info(self) -> None:
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self._color}')
        print(f'Владелец: {self._owner}')
        print(f'Количество пассажиров: {self.__PASSENGERS_LIMIT}')

    """
    def set_color(self, new_color: str) -> None:
        for color in self.COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self._color = new_color
                return print(f'Цвет сменен на {new_color}')
            else:
                return print(f"Нельзя сменить цвет на {new_color}")
    """

if __name__ == '__main__':
    # Мои тесты
    """ 
    car = Vehicle('Tormozzz','Oka', 45, 'blue')
    car.get_color
    car.change_color('grEEn')
    car.get_color
    car.print_info()
    #car.COLOR_VARIANTS.append('orange')
    """

    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'red', 500)
    vehicle1.set_color('black')

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'
    vehicle1.get_color
    # Проверяем что поменялось
    vehicle1.print_info()

