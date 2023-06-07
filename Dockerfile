# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the working directory
COPY hello_world.py .

# Set the entry point for the container
ENTRYPOINT ["python", "hello_world.py"]

