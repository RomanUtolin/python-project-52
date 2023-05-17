#makefile

start:
	poetry run python manage.py runserver 0.0.0.0:8000

install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 task_manager

translate:
	poetry run django-admin makemessages -l ru

comp_trans:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell
