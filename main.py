import os
import re
import requests
import typer
from datetime import datetime


from models import Vault, Note, Script

URL = "http://localhost:5000"

app = typer.Typer()


@app.command()
def convert(file: str):
    response = requests.post(URL, files={"file": open(file, "rb")})
    try:
        os.remove(file.replace(".fountain", ".pdf"))
    except FileNotFoundError:
        pass
    with open(file.replace(".fountain", ".pdf"), "wb") as f:
        f.write(response.content)


@app.command()
def parse_vault(path: str, version: str = "0", nct: bool = False):
    vault = Vault(path, version, nct)
    save_path = os.path.join(os.getcwd(), f"{vault.title.replace(' ', '_')}_V{version}.fountain")
    vault.save(save_path)
    convert(save_path)
    os.remove(save_path)


@app.command()
def parse_note(path):
    note = Note(path)
    script = Script(title=note.name, chapters_notes=[note])
    save_path = os.path.join(os.getcwd(), f"{script.title.replace(' ', '_')}.fountain")
    script.save(save_path)
    convert(save_path)
    os.remove(save_path)


if __name__ == '__main__':
    app()
