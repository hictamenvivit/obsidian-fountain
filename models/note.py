import os


class Note:

    @staticmethod
    def parse_for_fountain(text):
        try:
            _, useful = text.split("@&", 1)
            fountain, rest = useful.split("&@", 1)
            return fountain + "\n" + Note.parse_for_fountain(rest)
        except ValueError:
            return ""

    def __init__(self, path):
        self.path = path
        with open(path) as f:
            self.content = f.read()
        self.name = os.path.basename(path).replace(".md", "")

    def extract_foutain(self):
        return self.parse_for_fountain(self.content)


class ChapterNote(Note):

    def __init__(self, path):
        try:
            super().__init__(path)
        except FileNotFoundError:
            content = """#chapitre

@&

&@"""
            with open(path, "w") as file:
                file.write(content)
            super().__init__(path)
