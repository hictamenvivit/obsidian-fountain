import datetime
import os
import re

from models import Note, Script, ChapterNote


class Vault:
    """
    an obsidian vault with flat structure
    """

    def __init__(self, path, version=0, no_chapters_titles=False, chapters_file="Chapitres.md"):
        self.path = path
        self.title = os.path.basename(os.path.normpath(path))
        self.chapters_file = chapters_file
        self.chapters_notes = [ChapterNote(os.path.join(path, c + ".md")) for c in self.chapters]
        self.script = Script(title=self.title, chapters_notes=self.chapters_notes, no_chapters_titles=no_chapters_titles,
                             version=version)

    @property
    def chapters(self):
        with open(os.path.join(self.path, self.chapters_file)) as f:
            return re.findall(r"\[\[([^\]]*)\]\]", f.read())

    def save(self, save_path):
        self.script.save(save_path)
