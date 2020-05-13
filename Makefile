init:
	pip install -r requirements.txt

check:
	flake8 features/
	python -m pylint features/
	pycodestyle features/

test:
	behave
