# Setup Instructions for Dockerized Django Project

## Prerequisites

1. Ensure you have Docker and Docker Compose installed on your server.
2. Clone the repository to your server.

## Installation

1. Navigate to the project directory:

    bash
    cd ~/aiseoapp1/
    

2. Build and start the Docker containers:

    bash
    docker-compose up --build -d
    

3. Run database migrations:

    bash
    docker-compose exec django python manage.py makemigrations
    docker-compose exec django python manage.py migrate
    

4. Create a superuser for the Django admin:

    bash
    docker-compose exec django python manage.py createsuperuser
    

5. Access the application in your browser at http://104.248.116.196:8000.

## Additional Commands

- To view logs:

    bash
    docker-compose logs -f
    

- To stop the containers:

    bash
    docker-compose down
    