from abc import ABC, abstractmethod
from model.note import Note


class DataService(ABC):

    @abstractmethod
    def create_note(self, note: Note):
        pass

    @abstractmethod
    def read_note(self, search_id: int):
        pass

    @abstractmethod
    def update_note(self, note, search_id):
        pass

    @abstractmethod
    def delete_note(self, search_id):
        pass

    @abstractmethod
    def delete_all_notes(self):
        pass
