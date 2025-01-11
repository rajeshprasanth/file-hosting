import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '/app/uploads')  # Default to /app/uploads inside Docker
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4'}
SECRET_KEY = os.getenv('SECRET_KEY')  # Get the secret key from environment variables

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper function to get file details
def get_all_files():
    return [{
        'filename': f,
        'size': os.path.getsize(os.path.join(UPLOAD_FOLDER, f)),
        'uploaded': datetime.fromtimestamp(os.path.getctime(os.path.join(UPLOAD_FOLDER, f))).strftime('%Y-%m-%d %H:%M:%S'),
        'modified': datetime.fromtimestamp(os.path.getmtime(os.path.join(UPLOAD_FOLDER, f))).strftime('%Y-%m-%d %H:%M:%S'),
    } for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]

# Routes
@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    files_per_page = 10
    all_files = get_all_files()
    total_files = len(all_files)

    # Pagination logic
    start = (page - 1) * files_per_page
    end = start + files_per_page
    files = all_files[start:end]
    total_pages = (total_files + files_per_page - 1) // files_per_page

    return render_template('index.html', files=files, page=page, total_pages=total_pages)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded', 'success')
        return redirect(url_for('index'))
    else:
        flash('File type not allowed', 'danger')
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        os.remove(file_path)
        flash(f'File {filename} deleted successfully', 'success')
    except FileNotFoundError:
        flash(f'File {filename} not found', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
