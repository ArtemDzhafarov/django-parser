## Parser - Django, DRF, Django-rq, PostgreSQL
### Dev flow
---
#### Project setup
1. create virtual environment: `python3 -m venv .env`
2. install requirements: `pip install --upgrade -r requirements.txt`
3. apply migrations: `python manage.py migrate`(this step goes after database setup mentioned below)
4. Run redis: `make redis-docker`
5. Run RQ worker: `make worker`
6. Run django: `python manage.py runserver`
---
#### Database setup
PostgreSQL connecting in config.settings
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
---
#### TODO
1. React.js
2. Dockerize app