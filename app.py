from flask import Flask, request, render_template
import os
from parser import parse_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return "No file uploaded"
    
    file = request.files["file"]

    if file.filename == "":
        return "No selected file"
    
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    contacts = parse_pdf(filepath)

    return {
        "contacts": [
            {
                "name": c.name,
                "phone": c.phone,
                "note": c.note
            }
            for c in contacts
        ]
    } # a Python Dictionary that contains a List of Dictionaries


if __name__ == "__main__":
    app.run(debug=True)