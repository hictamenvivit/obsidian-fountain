import datetime
import os
import re

from models import Note, Script


class Vault:
    """
    an obsidian vault with flat structure
    """

    def __init__(self, path, chapters_file="Chapitres.md"):
        self.path = path
        self.title = os.path.basename(os.path.normpath(path))
        self.chapters_file = chapters_file
        self.chapters_notes = [Note(os.path.join(path, c + ".md")) for c in self.chapters]
        self.script = Script(title=self.title, chapters_notes=self.chapters_notes)


    @property
    def chapters(self):
        with open(os.path.join(self.path, self.chapters_file)) as f:
            return re.findall(r"\[\[([^\]]*)\]\]", f.read())

    def extract_fountain(self):
        return self.script.as_fountain()

    def save(self, save_path):
        self.script.save(save_path)
