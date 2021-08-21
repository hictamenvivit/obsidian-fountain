from flask import Flask, request, send_from_directory, send_file

app = Flask(__name__)
import os


@app.route("/", methods=["POST", "GET"])
def convert():
    if request.method == "GET":
        return "get"
    if request.method == "POST":
        file = request.files["file"]
        # os.remove("/tmp/*.pdf")
        save_path = os.path.join("/tmp", file.filename)
        file.save(save_path)
        try:
            os.remove(save_path.replace('.fountain', '.pdf'))
        except FileNotFoundError:
            pass

        os.system(
            f"afterwriting --source {save_path} --pdf {save_path.replace('.fountain', '.pdf')}")

        return send_file(save_path.replace(".fountain", ".pdf"))
    return "else"


if __name__ == '__main__':
    app.run("0.0.0.0")
