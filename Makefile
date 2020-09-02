.PHONY: all build start stop restart clean bash log migrations migrate makemessages compilemessages collectstatic cachetable superuser

# TODO
#CONTAINER=$(basename `pwd` | sed "s/[^[:alnum:]]//g")
CONTAINER=djangoinit

# https://docs.docker.com/compose/reference/build/
build:
	docker-compose build --parallel
	# --force-rm
	# --no-cache

# https://docs.docker.com/engine/reference/commandline/exec/
bash:
	docker exec -it ${CONTAINER} /bin/bash

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

log:
	docker-compose logs -f

start:
	docker-compose up -d --remove-orphans

stop:
	docker-compose down

restart:
	docker-compose down && docker-compose up -d

migrations:
	docker exec -it ${CONTAINER} python manage.py makemigrations

migrate:
	docker exec -it ${CONTAINER} python manage.py migrate

messages:
	docker exec -it ${CONTAINER} python manage.py makemessages -f venv/

compilemessages:
	docker exec -it ${CONTAINER}} python manage.py compilemessages

collectstatic:
	docker exec -it ${CONTAINER} python manage.py collectstatic

cachetable:
	docker exec -it ${CONTAINER} python manage.py createcachetable

superuser:
	docker exec -it ${CONTAINER} python manage.py createsuperuser