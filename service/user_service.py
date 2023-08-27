from service.data_service import DataService
from model.note import Note
from model.base_file import BaseFile


class UserService(DataService):

    def __init__(self, model: BaseFile):
        self.model: BaseFile = model
        self.notes: list = self.model.read_file()

    def create_note(self, note: Note):
        for item in self.notes:
            if item.id == note.id:
                note.id = item.id + 1
        self.notes.append(note)
        self.model.write_file(self.notes)

    def read_note(self, search_id: int) -> Note:
        for note in self.notes:
            if note.id == search_id:
                return note
            else:
                print("The record was not found,\n the index may be incorrectly specified")

    def update_note(self, note: Note, search_id: int) -> bool:
        for item in self.notes:
            if search_id == item.id:
                item.date = note.date
                item.title = note.title
                item.text = note.text
                self.model.write_file(self.notes)
                return True
        return False

    def delete_note(self, search_id) -> bool:
        for i, note in enumerate(self.notes):
            if note.id == search_id:
                del self.notes[i]
                self.model.write_file(self.notes)
                return True
        return False

    def delete_all_notes(self):
        self.notes.clear()
        self.model.write_file(self.notes)
