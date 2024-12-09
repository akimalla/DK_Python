
# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата "Книга 'название_книги'".
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает валидную строку для инициализации экземпляра.

        :return: Строка формата Book(id_=1, name='test_name_1', pages=200).
        """
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__