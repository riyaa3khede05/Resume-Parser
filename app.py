from flask import Flask, render_template, request
import os
import pdfplumber

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():

    extracted_text = ""

    if request.method == "POST":

        file = request.files["resume"]

        if file.filename != "":

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            with pdfplumber.open(filepath) as pdf:

                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"

    return render_template("index.html", text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)