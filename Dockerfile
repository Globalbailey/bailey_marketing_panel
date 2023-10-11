# Use the official Python image as the base image
FROM python:3.11

# Create and set the working directory in the container
WORKDIR /app

# Copy the project's requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the entire Django project directory into the container
COPY . .

# Expose the port on which your Django app will run (typically 8000)
EXPOSE 8000

# Specify the command to run your Django development server
CMD python manage.py runserver
