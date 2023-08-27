from controller.controller import Controller
from model.json_model import ModelJson
from service.user_service import UserService
from view.user_view import View


def run():
    print("Welcome to the notes app!")
    c = Controller(UserService(ModelJson("data_base.json")), View())
    while True:
        action = c.main_page()
        match action:
            case 1:
                c.create_note()
            case 2:
                c.read_note()
            case 3:
                c.update_note()
            case 4:
                c.del_note()
            case 5:
                c.del_all_notes()
            case 6:
                c.read_all_notes()
            case 7:
                c.file_save()
            case 8:
                print("All the best!")
                break
