from model.json_model import ModelJson
from model.note import Note
from service.user_service import UserService
from view.user_view import View


class Controller:
    def __init__(self, service: UserService, view: View):
        self.service = service
        self.view = view

    def create_note(self):
        id, date, title, text = self.view.create_note()
        self.service.create_note(Note(id, date, title, text))
        print("Entry added")

    def read_note(self):
        print(self.service.read_note(self.view.read_note()))

    def read_all_notes(self):
        self.view.read_all_notes(self.service.notes)

    def update_note(self):
        update_id, note = self.view.update_note()
        self.service.update_note(update_id, note)
        print("The record has been updated")

    def del_note(self):
        self.service.delete_note(self.view.del_note())
        print("Record deleted")

    def del_all_notes(self):
        self.service.delete_all_notes()
        print("All entries have been deleted")


c = Controller(UserService(list(), ModelJson("test.json")), View())
c.create_note()
c.read_note()
