
runserver:
	poetry run python src/manage.py runserver


migrate:
	poetry run python src/manage.py migrate


superuser:
	poetry run python src/manage.py createsuperuser


test:
	poetry run python src/manage.py test

