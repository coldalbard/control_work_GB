import json
from note import Note
from base_file import BaseFile


class ModelJson(BaseFile):

    def __init__(self, file_name: str):
        super().__init__(file_name)

    def read_file(self):
        notes_list = list()
        try:
            with open(self.file_name, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['title'], item['text']))

            return notes_list
        except FileNotFoundError:
            return self.notes

    def write_file(self, notes: list):
        json_strings_list = self.notes
        for note in notes:
            json_strings_list.append({'id': note.id, 'date': note.date, 'title': note.title, 'text': note.text})

        notes_json = json.dumps(json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.file_name, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)