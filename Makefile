codestyle-check:
	find . -name \*.py -exec pycodestyle --config=setup.cfg {} +
	
init:
	sudo pip install -r requirements.txt