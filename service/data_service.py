from abc import ABC, abstractmethod
from model.note import Note


class DataService(ABC):

    @abstractmethod
    def _create_note(self, note: Note):
        pass

    @abstractmethod
    def _read_note(self, search_id: int):
        pass

    @abstractmethod
    def _update_note(self, note, search_id):
        pass

    @abstractmethod
    def _delete_note(self, search_id):
        pass

    @abstractmethod
    def _delete_all_notes(self):
        pass
