from abc import ABC, abstractmethod
from model.note import Note


class DataService(ABC):

    @abstractmethod
    def create_note(self, note: Note):
        pass

    @abstractmethod
    def read_note(self, search_id: int) -> Note:
        pass

    @abstractmethod
    def update_note(self, note: Note, search_id: int) -> bool:
        pass

    @abstractmethod
    def delete_note(self, search_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_notes(self):
        pass
