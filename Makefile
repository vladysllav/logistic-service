migrate:
	docker-compose -f docker-compose.yml run web poetry run python src/manage.py migrate

test:
	docker-compose -f docker-compose.yml run web poetry run python src/manage.py test
