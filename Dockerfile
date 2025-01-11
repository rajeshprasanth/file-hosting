# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY app.py requirements.txt /app/
COPY templates /app/templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create upload folder
RUN mkdir -p /app/uploads

# Expose port
EXPOSE 5000

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
