from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
PDF_DIR = "pdfs"

@app.route("/")
def index():
    pdf_files = [
        {"name": f, "path": f"{PDF_DIR}/{f}"}
        for f in os.listdir(PDF_DIR)
        if f.endswith(".pdf")
    ]
    return render_template("index.html", pdf_files=pdf_files)

@app.route("/pdfs/<path:filename>")
def serve_pdf(filename):
    return send_from_directory(PDF_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
