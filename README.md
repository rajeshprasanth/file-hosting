# File Hosting

The **File Hosting** project is a Flask-based web application designed to facilitate the secure upload, storage, and management of files. It offers a user-friendly interface for users to upload, view, and delete files, making it an ideal solution for personal or small-scale file hosting needs.

## Features

- **File Upload:** Easily upload files through a simple web interface.
- **File Management:** View a list of uploaded files with details such as filename, size, and upload date.
- **File Deletion:** Remove unwanted files directly from the application.
- **Secure Storage:** Uploaded files are stored securely on the server.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rajeshprasanth/file-hosting.git
cd file-hosting
```
### 2. Set Up the Environment

Create a virtual environment and activate it:
 * On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

 * On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables

Create a .env file in the project root directory and add the following lines:

UPLOAD_FOLDER=uploads
SECRET_KEY=your_secret_key_here

Replace your_secret_key_here with a secure, random string.
5. Run the Application

python app.py

The application will start, and you can access it at http://localhost:5000.
Docker Setup

To run the application using Docker, follow these steps:
1. Build the Docker Image

docker build -t file-hosting .

2. Run the Docker Container

docker run -d -p 5000:5000 --name file-hosting file-hosting

This command runs the container in detached mode, maps port 5000 of the container to port 5000 on your host, and names the container file-hosting.
Usage

    Upload Files: Navigate to the homepage and use the upload form to select and upload files.
    View Files: After uploading, the files will appear in a list with details.
    Delete Files: Click the delete button next to a file to remove it from the server.

Contributing

Contributions are welcome! To contribute:

    Fork the repository.
    Create a new branch.
    Make your changes and commit them.
    Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For questions or feedback, please open an issue on the GitHub repository.

Thank you for using the File Hosting application!
