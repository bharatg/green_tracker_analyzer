# green_tracker_analyzer
Python 3 analyzer for green_tracker

## Useful Links
http://www.postgresqltutorial.com/postgresql-python/

- Local File: `database.ini`
- content
```
[postgresql]
host=localhost
database=suppliers
user=postgres
password=postgres
```

## To install first time venv. `python` runs python 3
```
python -m venv venv
```
run the environment with 
```
source venv/bin/activate
```
install dependencies locally
```
pip install -r ./requirements.txt
```
run server
```
python manage.py runserver
```

#### Heroku docs on Django
https://devcenter.heroku.com/articles/django-memcache

#### Django guide
https://docs.djangoproject.com/en/dev/intro/tutorial01/
