class Note:

    def __init__(self, content=None):
        self.content = content

    def write_note(self, content):
        self.content = content

    def delete_note(self):
        self.content = ""

    def __str__(self):
        return self.content


class Notebook:

    def __init__(self, title):
        self.title = title
        self.notes = []
        self.num_of_pages = 0

    def add_note(self, note):
        if self.num_of_pages < 5 and note is not None:
            self.notes.append(note)  # 1 page == 1 note
            self.num_of_pages += 1
        else:
            print("NO MORE PAGES LEFT!!!")

    def remove_note(self, note):

        if note in self.notes:
            self.notes.remove(note)
            self.num_of_pages -= 1
            print("note : ", id(note), " was deleted")
        else:
            print("there is no such note")

    def get_number_of_pages(self):
        print("current number of pages : ", self.num_of_pages)



