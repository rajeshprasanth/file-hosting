# File Hosting

The **File Hosting** project is a Flask-based web application designed to facilitate the secure upload, storage, and management of files. It offers a user-friendly interface for users to upload, view, and delete files, making it an ideal solution for personal or small-scale file hosting needs.

## Features

1. **User-Friendly Interface:** Built with Flask for a simple and intuitive design.
2. **File Upload & Management:** Supports uploading, listing, and deleting files.
3. **Secure Storage:** Ensures secure handling and storage of uploaded files.
4. **Flexible Deployment Options:** Supports local execution, virtual environments, and Docker-based deployments.
5. **Remote & Local Execution:** Run directly, inside a virtual environment, or as a Docker container.

## Installation & Usage

### 1. Clone the Repository

To begin using this application, clone the repository using the following command:

```bash
git clone https://github.com/rajeshprasanth/file-hosting.git
cd file-hosting
```

### 2. Installation and Execution Methods

Depending on your setup, you may choose one of the following installation methods:

#### Option 1: Direct Host Installation (Without Docker)

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the file hosting service at: `http://localhost:5000`

#### Option 2: Virtual Environment Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access the file hosting service at: `http://localhost:5000`

#### Option 3: Local Docker Build

1. Build and deploy the application using Docker:
   ```bash
   docker compose -f docker-compose.local.yml up -d
   ```
   - This command builds the image and starts the container in detached mode (`-d`).
   - Ensure the upload folder is correctly mounted.
2. Monitor logs:
   ```bash
   docker logs -f <container_id>
   ```
3. Access the file hosting service at: `http://localhost:5000`

#### Option 4: Deploy Using a Pre-Built Docker Image (Remote Image from Docker Hub)

1. Pull and deploy the latest pre-built image from Docker Hub:
   ```bash
   docker compose -f docker-compose.remote.yml up -d
   ```
2. To update the image:
   ```bash
   docker compose -f docker-compose.remote.yml pull
   ```
   ```bash
   docker compose -f docker-compose.remote.yml up -d --force-recreate
   ```
3. Access the file hosting service at: `http://localhost:5000`

### 3. Managing the Service

1. **Stopping the Service**
   ```bash
   docker compose down
   ```
2. **Restarting the Service**
   ```bash
   docker compose up -d --build
   ```
3. **Viewing Running Containers**
   ```bash
   docker ps
   ```

## Configuration

### 1. Volumes:
```yaml
volumes:
  - ./uploads:/app/uploads
```
- This ensures that uploaded files persist even after the container restarts.

### 2. Environment Variables:
```yaml
environment:
  - UPLOAD_FOLDER=/app/uploads
  - SECRET_KEY=supersecretkey
```
- `UPLOAD_FOLDER`: Specifies the directory for storing uploaded files.
- `SECRET_KEY`: Used by Flask for session management and security.

### 3. Ports:
```yaml
ports:
  - "5001:5000"
```
- Maps port 5000 inside the container (where the app runs) to port 5001 on your computer.
- Access the app at `http://localhost:5001`.

## Contributing

Contributions are welcome! If you would like to enhance the project, please submit a pull request or open an issue.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details. 
See the [LICENSE](LICENSE) file for details.
Thank you for using the File Hosting application!

