from model.note import Note
from service.user_service import UserService
from view.user_view import View


class Controller:
    def __init__(self, service: UserService, view: View):
        self.service = service
        self.view = view

    def create_note(self):
        self.service.create_note(self.view.create_note())
