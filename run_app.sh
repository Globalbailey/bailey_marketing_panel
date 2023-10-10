#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker to run this application."
    exit 1
fi

# Build the Docker containers
docker-compose build

# Apply database migrations
docker-compose run django-cli makemigrations
docker-compose run django-cli migrate

# Start the Django development server
docker-compose up -d web

echo "The application is now running at http://localhost:8000/"
echo "You can stop the server with 'docker-compose down' when you're done."
