PHONY: black run

black:
	black .
	@echo "Black reformatted!!!"

run:
	python manage.py runserver
	@echo "Run starting!!!"
