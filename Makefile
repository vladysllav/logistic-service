
runserver:
	poetry run python src/manage.py runserver


migrate:
	poetry run python src/manage.py migrate


tests:
	poetry run python src/manage.py test
