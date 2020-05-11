CONTAINER_NAME ?= requests
CMD ?= bash


check:
	flake8 features/
	pylint features/
	pycodestyle features/

test:
	$(MAKE) shell CMD='behave'
