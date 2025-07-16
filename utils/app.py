from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

from utils.transcriber import *
from utils.pdf_generator import *
from utils.email_sender import *

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    emails = request.form['emails'].split(',')

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    text = transcribe_audio(filepath)
    if "Transcription failed" in text:
        return jsonify({"error": text}), 500

    pdf_path = save_as_pdf(text, filename + ".pdf")
    send_email(emails, pdf_path)

    return jsonify({"message": "Meeting minutes sent successfully."})

if __name__ == '__main__':
    app.run(debug=True)
