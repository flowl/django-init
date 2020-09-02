
# django-init

`django-init` is a Django 3 starting template that allows you to kickstart a project without setup hassle and complexity, while maintaining a best practice project structure with up to date dependencies.


## Package contains

- Django 3 (`Django>=3.0`)
- Python (`python:3.8-slim`)
- MariaDB server/client (`mariadb:10.5-focal`)
- `sqlite3` (default, see [settings.py](apps/Application/settings.py))
- `netcat` as a dependency of [`wait-for`](https://github.com/eficode/wait-for)
- [`requirements.txt`](requirements.txt)

### Features

- Custom default User ([Django 3 implementation](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model))
- .env file support (https://github.com/joke2k/django-environ)
- The username is the email address (How do you like this?)
- Preconfigured settings for SMTP, MySQL, sqlite3, caching, ...
- i18n enabled and substituted `datetime.now()` by `timezone.now()`
- "hello world" view and template


## Installation

This template is preconfigured to work with `docker-compose` out of the box ([see docker-compose.yml](docker-compose.yml)).
For best performance, the executed code is mounted host authoritive (`cached`) while the MySQL data files are mounted container authoritive (`delegated`). 

    $ git clone https://github.com/flowl/django-init
    $ cd django-init/
    $ make build
    
**Go to [`settings.py`](apps/Application/settings.py) and add a long random string to `SECRET_KEY`.**
    
Initial migrations:
    
    $ make migrate
    
Create a superuser and the cache table:

    $ make shell
    $ python manage.py createcachetable
    $ python manage.py createsuperuser
    $ exit

Start:
    
    $ make start
    $ make log
    
Then visit [`http://djangoinit.localhost:8022`](http://djangoinit.localhost:8022).

If you have [`traefik`](https://docs.traefik.io/) installed, you can also go to [`http://djangoinit.localhost`](http://djangoinit.localhost) straight.

**The admin url is http://djangoinit.localhost/en/admin/** 


## Settings

Please edit [`apps/Application/settings.py`](apps/Application/settings.py), especially the following:

- `SECRET_KEY`, `AUTH_PASSWORD_VALIDATORS`
- `DEBUG`, `ALLOWED_HOSTS`
- `DATABASES` (MySQL container and sqlite3)
- `CACHES` (using MySQL)
- `EMAIL_BACKEND` and SMTP settings
- `USE_I18N`, `USE_L10N`, `USE_TZ`

## Hints

See the [`Makefile`](Makefile) for available commands.


---


https://github.com/flowl/django-init


Maintained by [Daniel Wendler](https://danielwendler.dev).

For development purpose.


<small>Distributed under the MIT License.</small>
