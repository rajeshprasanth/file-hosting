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

### 2. Docker Setup

To run the application using Docker, follow these steps:

#### 1. Local Build

To build the Docker image locally, follow these steps:

#### Build the Docker Image

```bash
docker build -t file-hosting .
```
#### Run the Docker Container
```bash
docker run -d -p 5000:5000 --name file-hosting file-hosting
```
This command runs the container in detached mode, maps port 5000 of the container to port 5000 on your host, and names the container file-hosting.

#### 2. Remote Pull

Alternatively, you can pull the pre-built image from Docker Hub and run the container:
#### Pull the Docker Image
```bash
docker pull rajeshprasanth/file-hosting:latest
```
#### Run the Docker Container
```bash
docker run -d -p 5000:5000 --name file-hosting rajeshprasanth/file-hosting:latest
```
This command pulls the image from Docker Hub and runs the container in detached mode, mapping port 5000 of the container to port 5000 on your host.
## Usage

### 1. Volumes:
```yaml
volumes:
  - ./uploads:/app/uploads
```
- This makes a folder on your computer (./uploads) available inside the container at /app/uploads.
- It allows files uploaded in the app to be saved on your computer, so they’re not lost when the container restarts.

### 2. Environment Variables:
```yaml
environment:
  - UPLOAD_FOLDER=/app/uploads
  - SECRET_KEY=supersecretkey
```
 - `UPLOAD_FOLDER`: Tells the app where to save uploaded files inside the container.
 - `SECRET_KEY`: A secret value used by Flask to handle things like sessions and cookies securely. You should change this to a more secure key.

### 3. Ports:
```yaml
ports:
  - "5001:5000"
```
 - Maps port 5000 inside the container (where the app runs) to port 5001 on your computer.
 - You can then access the app by going to http://localhost:5001 in your web browser.


## License

This Docker image is provided under the MIT License. See the LICENSE file for more information.

## Contributions

If you would like to contribute to this project, feel free to submit a pull request or open an issue. We welcome bug fixes, feature improvements, and any suggestions to make this Docker image even better!

Thank you for using the File Hosting application!


