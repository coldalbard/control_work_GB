import csv
from note import Note
from base_file import BaseFile


class ModelCsv(BaseFile):

    def __init__(self, file_name: str):
        super().__init__(file_name)

    def read_file(self):
        notes_list = list()
        try:
            data = list()
            with open(self.file_name, newline='') as my_file:
                reader = csv.reader(my_file, delimiter=',', quoting=csv.QUOTE_NONE)
                for row in reader:
                    data.append(row)
            for item in data:
                notes_list.append(Note(int(item[0]), item[1], item[2], item[3]))

            return notes_list
        except ValueError:
            return self.notes

    def write_file(self, notes: list):
        csv_list = list()
        for note in notes:
            csv_list.append([note.id, note.date, note.title, note.text])
        with open(self.file_name, "a",  newline="") as my_file:
            writer = csv.writer(my_file)
            writer.writerows(csv_list)
