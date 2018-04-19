# TODO
- [ ] Understand exactly how can Telegram/node talk to the python app/dyno
- [ ] Write some tests (using some suitable python module)
- [ ] Landing page with django
- [ ] Setting up migrations
- [ ] Decide where to show the statistics (push them on Telegram? Show them at some url in the django or the node site?)
- [ ] Decide what and how to visualize it (which statistics to show, and the visualization design)
- [ ] Setup multiple databases on django (one remote on heroku, one local, using django-environ and .env files)
- [x] Cleanup in the repo. Remove what is unneeded.
- [ ] Django minimal app (correctly set up app, at least index for / url)
- [x] Solving 'gunicorn' bug and making the app run on heroku
- [x] Setting up correctly config variables on heroku
- [x] Python app on heroku (working locally)

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
