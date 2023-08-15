class Note(object):
    def __init__(self, id, title, text, date):
        self.id = id
        self.title = title
        self.text = text
        self.date = date

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        self.title = title

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, text):
        self.text = text

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, date):
        self.date = date

    def __str__(self):
        return f'\nЗаметка: {self.id}\nДата создания(редактирования):' \
               f' {self.date}\nЗаголовок: {self.title}\nТело: {self.text}\n'
