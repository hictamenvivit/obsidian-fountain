import os
import re
import requests
import typer
from datetime import datetime

from models import Vault

URL = "http://localhost:5000"

app = typer.Typer()


@app.command()
def convert(file: str):
    response = requests.post(URL, files={"file": open(file, "rb")})
    try:
        os.remove(file.replace(".fountain", ".pdf"))
    except:
        pass
    with open(file.replace(".fountain", ".pdf"), "wb") as f:
        f.write(response.content)


@app.command()
def parse_vault(path: str):
    vault = Vault(path)
    save_path = os.path.join(os.getcwd(), f"{vault.title.replace(' ', '_')}.fountain")
    vault.save(save_path)
    convert(save_path)
    os.remove(save_path)


if __name__ == '__main__':
    app()
