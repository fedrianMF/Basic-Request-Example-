init:
	pip install -r requirements.txt

check:
	flake8 features/
	flake8 main/
	pylint features/
	pylint main/
	pycodestyle features/
	pycodestyle main/

test:
	behave
