PHONY: black run test test_time

black:
	black .
	@echo "Black reformatted!!!"

run:
	python manage.py runserver
	@echo "Run starting!!!"

test:
	pytest -v -s
	@echo "Testing!!!"

test_time:
	pytest -v -s --durations=0
	@echo "Testing time tracking!!!"

test_parameter:
	pytest ./companies/tests/test_unittest_api.py -k $(arg)
	@echo "Testing add string parameter!!!"