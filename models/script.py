import datetime


class Script:

    def __init__(self, title, chapters_notes):
        self.title = title
        self.chapters_notes = chapters_notes

    @property
    def header(self):
        today = datetime.date.today().strftime('%Y-%m-%d')
        return f"""Title:
    _**{self.title}**_
Credit: Written by
Author: Maxime Bettinelli
Draft date: {today}
"""

    def as_fountain(self):
        return self.header + "\n\n\n\n" + "\n\n".join([f"*** Chapitre {i}: {note.name} ***" + note.extract_foutain() for (i, note) in
                                          enumerate(self.chapters_notes)])

    def save(self, save_path):
        with open(save_path, "w") as f:
            f.write(self.as_fountain())
