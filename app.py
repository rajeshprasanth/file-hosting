from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify
import os
import datetime

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
FILES_PER_PAGE = 5  # Files per page for pagination

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check if the file type is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to get file information
def get_file_info(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        uploaded_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        return {
            'filename': filename,
            'size': file_size,
            'uploaded': uploaded_time.strftime('%Y-%m-%d %H:%M:%S'),
            'modified': modified_time.strftime('%Y-%m-%d %H:%M:%S')
        }
    return None

@app.route('/')
def index():
    # Pagination logic
    page = request.args.get('page', 1, type=int)
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files_info = [get_file_info(file) for file in files]
    
    # Sort files by upload date (most recent first)
    files_info.sort(key=lambda x: x['uploaded'], reverse=True)
    
    # Pagination
    start = (page - 1) * FILES_PER_PAGE
    end = start + FILES_PER_PAGE
    paginated_files = files_info[start:end]
    
    total_files = len(files_info)
    total_pages = (total_files // FILES_PER_PAGE) + (1 if total_files % FILES_PER_PAGE else 0)
    
    return render_template('index.html', files=paginated_files, page=page, total_pages=total_pages)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    else:
        return "File type not allowed", 400

@app.route('/files', methods=['GET'])
def get_files():
    # Return the list of files in the upload folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files_info = [get_file_info(file) for file in files]
    return jsonify({'files': files_info})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'message': f"File {filename} deleted successfully"}), 200
    else:
        return jsonify({'message': f"File {filename} not found"}), 404

if __name__ == '__main__':
   app.run(debug=True,port=5001)
