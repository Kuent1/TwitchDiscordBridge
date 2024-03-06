# Use the official Python base image
FROM python:3.9-slim

# Install Docker Compose
RUN pip install docker-compose

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python application code to the container
COPY app.py .

# Set the command to run the Python application
CMD ["python", "app.py"]