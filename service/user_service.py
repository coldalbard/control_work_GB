from data_service import DataService
from model.note import Note
from model.base_file import BaseFile


class UserService(DataService):

    def __init__(self, notes: list, model: BaseFile):
        self.notes = notes
        self.model = model

    def _create_note(self, note: Note):
        id = 0
        for item in self.notes:
            if item.id > id:
                id = item.id
        note.id = id + 1
        self.notes.append(note)
        self.model.write_file(self.notes)

    def _read_note(self, search_id: int):
        for note in self.notes:
            if note.id == search_id:
                return note
            else:
                print("The record was not found,\n the index may be incorrectly specified")

    def _update_note(self, note, search_id):
        for item in self.notes:
            if search_id == item.id:
                item.date = note.date
                item.title = note.title
                item.text = note.text
        self.model.write_file(self.notes)

    def _delete_note(self, search_id):
        for i, note in enumerate(self.notes):
            if note.id == search_id:
                del self.notes[i]
        self.model.write_file(self.notes)

    def _delete_all_notes(self):
        self.notes.clear()
        self.model.write_file(self.notes)
