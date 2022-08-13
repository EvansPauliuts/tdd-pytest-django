PHONY: black run test test_time test_cov

black:
	black .
	@echo "Black reformatted!!!"

run:
	python manage.py runserver
	@echo "Run starting!!!"

test:
	pytest -v -s
	@echo "Testing!!!"

test_cov:
	pytest -s -v --durations=0 --cov=.
	@echo "Testing cov!!!"

test_time:
	pytest -v -s --durations=0
	@echo "Testing time tracking!!!"

test_parameter:
	pytest ./companies/tests/test_unittest_api.py -k $(arg)
	@echo "Testing add string parameter='parameter'!!!"

test_arg:
	pytest -v -s --durations=0 -k $(arg)
	@echo "Testing add string arg='arg'!!!"

test_class_method:
	pytest -v -s --durations=0 ./companies/tests/test_unittest_api.py::TestGetCompanies::test_zero_companies_should_return_empty_list