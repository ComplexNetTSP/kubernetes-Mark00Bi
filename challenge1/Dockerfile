FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask app into the container
COPY app.py /app/

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]

