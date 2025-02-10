#!/bin/sh

#echo "Installing dependencies..."
pip install -r requirements.txt

#echo "Applying database migrations..."
python manage.py migrate

#echo "Collecting static files..."
python manage.py collectstatic --noinput

#echo "Starting the Django application..."
#gunicorn your_project.wsgi:application


unicorn project.wsgi:application
