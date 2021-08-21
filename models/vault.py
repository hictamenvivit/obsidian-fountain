import datetime
import os
import re

from models import Note


class Vault:
    """
    an obsidian vault with flat structure
    """

    def __init__(self, path, chapters_file="Chapitres.md"):
        self.path = path
        self.title = os.path.basename(os.path.normpath(path))
        self.chapters_file = chapters_file
        self.chapters_notes = [Note(os.path.join(path, c + ".md")) for c in self.chapters]

    @property
    def header(self):
        today = datetime.today().strftime('%Y-%m-%d')
        return f"""Title:
    _**{self.title}**_
Credit: Written by
Author: Maxime Bettinelli
Draft date: {today}
    
"""

    @property
    def chapters(self):
        with open(os.path.join(self.path, self.chapters_file)) as f:
            return re.findall(r"\[\[([^\]]*)\]\]", f.read())

    def extract_fountain(self):
        return "\n\n".join([f"*** Chapitre {i}: {note.name} ***" + note.extract_foutain() for (i, note) in
                            enumerate(self.chapters_notes)])

    def save(self, save_path):
        with open(save_path, "w") as f:
            f.write(self.extract_fountain())
