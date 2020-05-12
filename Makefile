init:
	pip install -r requirements.txt

check:
	flake8 task/*.py
	pycodestyle task/*.py
	pylint task/*.py
