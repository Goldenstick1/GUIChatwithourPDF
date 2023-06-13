from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({ 'error': 'No file part' })
    file = request.files['file']
    if file.filename == '':
        return jsonify({ 'error': 'No selected file' })
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({ 'filename': filename })

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    # Generate a response using your model here.
    response = "Your model's response goes here."
    return jsonify({ 'message': response })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
