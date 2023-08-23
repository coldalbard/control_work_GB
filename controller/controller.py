from model.note import Note
from service.user_service import UserService
from view.user_view import View


class Controller:
    def __init__(self, service: UserService, view: View):
        self.service = service
        self.view = view

    def create_note(self):
        self.service.create_note(Note(self.view.create_note()))
        print("Entry added")

    def read_note(self):
        print(self.service.read_note(self.view.read_note()))

    def update_note(self):
        self.service.update_note(self.view.update_note())
        print("The record has been updated")

    def del_note(self):
        self.service.delete_note(self.view.del_note())
        print("Record deleted")

    def del_all_notes(self):
        self.service.delete_all_notes()
        print("All entries have been deleted")