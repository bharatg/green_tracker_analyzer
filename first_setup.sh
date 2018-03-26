#!/bin/bash
#mkdir analyzer && cd analyzer
python -m venv venv    # For Python 2 use `virtualenv venv`
source venv/bin/activate
pip install Django django-heroku gunicorn
django-admin.py startproject analyzer .
pip freeze > requirements.txt
python manage.py runserver
#source venv/bin/activate
#pip install -r ./requirements.txt
# python manage.py runserver
