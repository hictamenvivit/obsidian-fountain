import os
import re

import requests
import typer
from datetime import datetime

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
def parse(file: str):
    with open(file) as f:
        content = f.read()
    if "{fountain}" not in content:
        print("No fountain in this file")
        return
    fountain = content.split("{fountain}")[1].split("{/fountain}")[0]

    save_path = file.replace(" ", "_") + ".fountain"

    with open(save_path, "w") as f:
        f.write(fountain)
    convert(save_path)
    os.remove(save_path)


@app.command()
def parse_vault(path: str):
    today = datetime.today().strftime('%Y-%m-%d')
    with open(os.path.join(path, "Chapitres.md")) as f:
        chapitres = re.findall(r"\[\[([^\]]*)\]\]", f.read())
    fountain_all = f"""Title:
    _**{os.path.basename(path)}**_
Credit: Written by
Author: Maxime Bettinelli
Draft date: {today}
    
    """
    for chapter_number, chapitre in enumerate(chapitres):
        with open(os.path.join(path, f"{chapitre}.md")) as f:
            content = f.read()
            if "{fountain}" not in content:
                continue
            fountain = content.split("{fountain}")[1].split("{/fountain}")[0]

            fountain_all += f"*** CHAPITRE {chapter_number} {chapitre} ***\n\n" + fountain
    save_path = os.path.join(os.getcwd(), f"{os.path.basename(path).replace(' ', '_')}.fountain")
    with open(save_path, "w") as f:
        f.write(fountain_all)
    convert(save_path)
    os.remove(save_path)


@app.command()
def print_me():
    print("joijio")


if __name__ == '__main__':
    app()
