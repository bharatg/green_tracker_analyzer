# TODO
- [ ] Understand exactly how can Telegram/node talk to the python app/dyno
- [ ] Write some tests (using some suitable python module)
- [ ] Landing page with django
- [ ] Setting up migrations
- [ ] Install modules for managing, analyzing, displaying data
- [ ] Decide where to show the statistics (push them on Telegram? Show them at some url in the django or the node site?)
- [ ] Decide what and how to visualize it (which statistics to show, and the visualization design)
- [ ] Trying connection and queries on local ad remote database
- [x] Setup local and remote database (used ignored settings_local.py and django-environ)
- [x] Cleanup the repo. Remove what is unneeded. Ignore what must be ignored. Clear the cached files in heroku remote.
- [ ] Django minimal app (correctly set up app, at least index for / url)
- [x] Solving 'gunicorn' bug and making the app run on heroku
- [x] Setting up correctly config variables on heroku
- [x] Python app on heroku (working locally)

# green_tracker_analyzer
Python 3 analyzer for green_tracker

## Useful Links
[postgreSQL python](http://www.postgresqltutorial.com/postgresql-python/)
[psycopg docs](http://initd.org/psycopg/docs/install.html#binary-install-from-pypi)
[django-environ](https://django-environ.readthedocs.io/en/latest/#environ-env)
[local vs production settings - db](https://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django)
[django settings](https://docs.djangoproject.com/en/2.0/ref/settings/)
[django getting started](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
[scaling a django application](https://devcenter.heroku.com/articles/django-memcache)

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

