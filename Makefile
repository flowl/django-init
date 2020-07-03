.PHONY: all build start stop restart clean bash log migrations migrate makemessages compilemessages

#CONTAINER=$(basename `pwd` | sed "s/[^[:alnum:]]//g")
CONTAINER=djangoinit

build:
	docker-compose build --force-rm
	# --no-cache

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
	docker exec -it ${CONTAINER} python manage.py makemessages

compilemessages:
	docker exec -it ${CONTAINER} python manage.py compilemessages
