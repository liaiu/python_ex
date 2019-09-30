from zip_module.document_case_study.cursor import Cursor
from zip_module.document_case_study.character import Character


class Document:

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        f = open(self.filename, 'w')
        f.write("".join(self.characters))
        f.close()

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))


d = Document()
t = "sdadfregregreg\nfdsfdsfsfd"
for x in range(len(t)):
    if x == 3:
        c = Character(t[x], bold=True)
    elif x == 6:
        c = Character(t[x], italic=True)
    elif x == 9:
        c = Character(t[x], underline=True)
    else:
        c = t[x]
    d.insert(c)
d.cursor.home()
d.insert("*")
print(d.string)