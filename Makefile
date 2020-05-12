init:
	pip install -r requirements.txt

check:
	flake8 *.py
	pycodestyle *.py
	pylint *.py
