# Use the official Python image as the base image
FROM python:3.x

# Create and set the working directory in the container
WORKDIR /app

# Copy the project's requirements.txt file into the container
COPY gmcmarketing/requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the entire Django project directory into the container
COPY gmcmarketing /app/

# Expose the port on which your Django app will run (typically 8000)
EXPOSE 8000

# Specify the command to run your Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
