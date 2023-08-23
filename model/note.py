class Note:
    def __init__(self, id: int, title: str, text: str, date):
        self.__id: int = id
        self.__title: str = title
        self.__text: str = text
        self.__date: str = date

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id: int = id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title: str = title

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text: str = text

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date: str = date

    def __str__(self):
        return f'\nЗаметка: {self.id}\nДата создания:' \
               f' {self.__date}\nЗаголовок: {self.__title}\nТело: {self.__text}\n'
