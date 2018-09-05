

up:
	@docker-compose  up -d

down:
	@docker-compose  down

build:
	@docker-compose  build


shell:
	@docker-compose  run webserver python manage.py shell

ps:
	@docker-compose  ps

webserver:
	@docker-compose exec webserver /bin/bash

database:
	@docker-compose  exec database /bin/bash


makemig:
	@docker-compose run webserver python manage.py makemigrations

mig:
	@docker-compose  run webserver python manage.py migrate

createsuperuser:
	@docker-compose  run webserver python manage.py createsuperuser

