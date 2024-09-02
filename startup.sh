#!/bin/bash
cd /home/site/wwwroot
python manage.py migrate
gunicorn --bind=0.0.0.0:8000 res_api_project.wsgi