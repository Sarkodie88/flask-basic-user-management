setup:
	python3 -m venv venv
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py tests
test:
	pytest -v
	coverage report -m

format:
	black *.py */*.py

all: setup install format test lint