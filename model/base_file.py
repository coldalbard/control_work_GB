from abc import ABC, abstractmethod


class BaseFile(ABC):
    def __init__(self, file_name: str):
        self.file_name = file_name

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, note: list):
        pass