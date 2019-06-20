class CoordiPair:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_xy(self):
        print(self.x, self.y)


class Notebook:

    author = None

    def __init__(self, title):
        self.title = title

    def who_is_author(self):
        print("the author of this note is %s" % self.author)

    def set_title(self, title):
        self.title = title

    def get_title(self):
        if self.title is None:
            print("no title")
        else:
            print(self.title)
            return self.title


class Calculator:

    def __init__(self, val=0):
        self.value = val

    def add(self, num):
        self.value += num
        return self.value


if __name__ == '__main__':

    point = CoordiPair(-3, 2)
    point2 = CoordiPair(4, 7)
    print("end")

    note = Notebook()
    note.author = "Sara"
    note.who_is_author()

    note.set_title("TITLE")
    note.get_title()

    # Notebook.get_title()
    # TypeError: get_title() missing 1 required positional argument: 'self'

    Notebook.get_title(note)  # self -> instance itself.

    note.title = "another TITLE"
    note.get_title()



