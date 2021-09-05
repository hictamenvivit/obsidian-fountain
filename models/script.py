import datetime


class Script:

    def __init__(self, title, chapters_notes, no_chapters_titles, version):
        self.title = title
        self.chapters_notes = chapters_notes
        self.no_chapters_titles = no_chapters_titles
        self.version = version

    @property
    def header(self):
        today = datetime.date.today().strftime('%Y-%m-%d')
        return f"""Title:
    _**{self.title} (V{self.version})**_
Credit: Written by
Author: Maxime Bettinelli
Draft date: {today}
"""

    def as_fountain(self):
        if self.no_chapters_titles:
            return self.header + "\n\n\n\n" + "\n\n".join([note.extract_foutain() for note in self.chapters_notes])
        return self.header + "\n\n\n\n" + "\n\n".join([f"*** Chapitre {i}: {note.name} ***" + note.extract_foutain() for (i, note) in
                                          enumerate(self.chapters_notes)])

    def save(self, save_path):
        with open(save_path, "w") as f:
            f.write(self.as_fountain())
