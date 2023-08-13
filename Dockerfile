# Use the specific Python alpine image from Docker Hub
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src/api /app
COPY requirements.txt /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
