# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install necessary dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code to the container
COPY . /app/

# Expose the port Flask is running on
EXPOSE 5000

# Run the app with gunicorn (production WSGI server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "server:app"]
