from datetime import datetime


class View:
    def main_Page(self) -> int:
        action = int(input('1 - create a note\n'
                           '2 - read the note\n'
                           '3 - update a note\n'
                           '4 - delete a note\n'
                           '5 - delete all notes\n'
                           '6 - read all notes\n'
                           '7 - save to file\n'
                           '8 - exit\n' +
                           'Select an action: '))
        return action

    def create_note(self) -> tuple[int, str, str, str]:
        title = input("Enter a title: ")
        text = input("Enter a note: ")
        date = datetime.today().strftime("%d%m%Y")
        return 1, title, text, date

    def read_note(self) -> int:
        search_id = int(input("Enter the id of the note to search for: "))
        return search_id

    def update_note(self) -> tuple[str, str, str]:
        return self.create_note()

    def del_note(self):
        search_id = int(input("Enter the id of the note to delete: "))
        return search_id

    def read_all_notes(self, notes: list):
        print()
        print("All notes: ")
        for note in notes:
            print(note)

    def file_save(self):
        file_format = input("Enter the format you want to save to (JSON, CSV): ").lower()
        if file_format != "json" or file_format != "csv" or not file_format:
            file_format = "json"
        file_name = input("Enter the file name: ")
        if not file_name:
            file_name = "file"
        print("Enter the path where you want to save the file,"
              "\nExample: D:\gb\control_work\model")
        path = input("Path: ")
        if not path:
            path = "D:\gb\control_work\model" + "\\" + file_name + "." + file_format
        else:
            path += "\\" + file_name + "." + file_format
        return path
