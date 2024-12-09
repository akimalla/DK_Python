import doctest

class Furniture(ABC):
    def __init__(self, material: str, weight: float):
        """
        Инициализация класса Furniture.

        :param material: Материал, из которого изготовлена мебель. Должен быть строкой.
        :param weight: Вес мебели в килограммах. Должен быть положительным числом.
        :raises ValueError: Если weight <= 0.
        """
        if weight <= 0:
            raise ValueError("Вес мебели должен быть положительным числом.")
        self.material = material
        self.weight = weight

    @abstractmethod
    def assemble(self) -> None:
        """
        Метод для сборки мебели.

        :return: None
        :doctest:
        >>> chair = Chair("дерево", 5)
        >>> chair.assemble()
        'Стул собран.'
        """
        ...

    @abstractmethod
    def disassemble(self) -> None:
        """
        Метод для разборки мебели.

        :return: None
        :doctest:
        >>> chair = Chair("дерево", 5)
        >>> chair.disassemble()
        'Стул разобран.'
        """
        ...


class Plant(ABC):
    def __init__(self, species: str, height: float):
        """
        Инициализация класса Plant.

        :param species: Вид растения. Должен быть строкой.
        :param height: Высота растения в сантиметрах. Должен быть положительным числом.
        :raises ValueError: Если height <= 0.
        """
        if height <= 0:
            raise ValueError("Высота растения должна быть положительным числом.")
        self.species = species
        self.height = height

    @abstractmethod
    def water(self, amount: float) -> None:
        """
        Метод для полива растения.

        :param amount: Количество воды в литрах. Должно быть положительным числом.
        :return: None
        :doctest:
        >>> cactus = Cactus("Кактус", 30)
        >>> cactus.water(0.5)
        'Кактус полит 0.5 литра воды.'
        """
        ...

    @abstractmethod
    def prune(self) -> None:
        """
        Метод для обрезки растения.

        :return: None
        :doctest:
        >>> cactus = Cactus("Кактус", 30)
        >>> cactus.prune()
        'Кактус обрезан.'
        """
        ...


class SocialMedia(ABC):
    def __init__(self, name: str, user_count: int):
        """
        Инициализация класса SocialMedia.

        :param name: Название социальной сети. Должен быть строкой.
        :param user_count: Количество пользователей. Должен быть неотрицательным целым числом.
        :raises ValueError: Если user_count < 0.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.user_count = user_count

    @abstractmethod
    def post_update(self, content: str) -> None:
        """
        Метод для публикации обновления.

        :param content: Содержимое обновления. Должно быть строкой.
        :return: None
        :doctest:
        >>> fb = Facebook("Facebook", 2000000000)
        >>> fb.post_update("Hello, world!")
        'Обновление опубликовано: Hello, world!'
        """
        ...

    @abstractmethod
    def delete_account(self, user_id: int) -> None:
        """
        Метод для удаления аккаунта пользователя.

        :param user_id: Идентификатор пользователя. Должен быть положительным целым числом.
        :return: None
        :doctest:
        >>> fb = Facebook("Facebook", 2000000000)
        >>> fb.delete_account(12345)
        'Аккаунт пользователя 12345 удален.'
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации