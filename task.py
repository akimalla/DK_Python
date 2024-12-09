class Vehicle:
    def __init__(self, id_: int, name: str, wheels: int):
        """
        Инициализация транспортного средства.

        :param id_: Идентификатор транспортного средства.
        :param name: Название транспортного средства.
        :param wheels: Количество колес.
        """
        self.id_ = id_
        self.name = name
        self._wheels = wheels  # Приватный атрибут, чтобы предотвратить его изменение извне

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строка формата "Транспортное средство: название".
        """
        return f'Транспортное средство: {self.name}'

    def __repr__(self) -> str:
        """
        Возвращает валидную строку для инициализации экземпляра.

        :return: Строка формата Vehicle(id_=1, name='название', wheels=4).
        """
        return f"Vehicle(id_={self.id_}, name='{self.name}', wheels={self._wheels})"

    def get_wheels(self) -> int:
        """
        Возвращает количество колес.

        :return: Количество колес.
        """
        return self._wheels


class Car(Vehicle):
    def __init__(self, id_: int, name: str, wheels: int, doors: int):
        """
        Инициализация легкового автомобиля.

        :param id_: Идентификатор легкового автомобиля.
        :param name: Название легкового автомобиля.
        :param wheels: Количество колес.
        :param doors: Количество дверей.
        """
        super().__init__(id_, name, wheels)  # Вызов конструктора базового класса
        self.doors = doors  # Атрибут, специфичный для легкового автомобиля

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строка формата "Легковой автомобиль: название, двери: количество".
        """
        return f'Легковой автомобиль: {self.name}, двери: {self.doors}'

    def get_wheels(self) -> int:
        """
        Возвращает количество колес, добавляя информацию о типе транспортного средства.

        :return: Количество колес.
        """
        return f'{self.name} имеет {self._wheels} колес(а)'  # Перегруженный метод


class Truck(Vehicle):
    def __init__(self, id_: int, name: str, wheels: int, capacity: float):
        """
        Инициализация грузовика.

        :param id_: Идентификатор грузовика.
        :param name: Название грузовика.
        :param wheels: Количество колес.
        :param capacity: Грузоподъемность в тоннах.
        """
        super().__init__(id_, name, wheels)  # Вызов конструктора базового класса
        self.capacity = capacity  # Атрибут, специфичный для грузовика

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузовика.

        :return: Строка формата "Грузовик: название, грузоподъемность: тоннаж".
        """
        return f'Грузовик: {self.name}, грузоподъемность: {self.capacity} тонн'

    def get_wheels(self) -> int:
        """
        Возвращает количество колес, добавляя информацию о типе транспортного средства.

        :return: Количество колес.
        """
        return f'{self.name} имеет {self._wheels} колес(а)'  # Перегруженный метод


if __name__ == "__main__":
    # Пример использования классов
    car = Car(id_=1, name='Toyota Camry', wheels=4, doors=4)
    truck = Truck(id_=2, name='Volvo FH', wheels=6, capacity=18.0)

    print(car)  # Проверяем метод __str__ для легкового автомобиля
    print(car.get_wheels())  # Проверяем перегруженный метод get_wheels

    print(truck)  # Проверяем метод __str__ для грузовика
    print(truck.get_wheels())  # Проверяем перегруженный метод get_wheels