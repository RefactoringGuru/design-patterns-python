codestyle-check:
	find . -name \*.py -exec pycodestyle --config=setup.cfg {} +
	
codestyle-fix:
	autopep8 -r . --global-config setup.cfg
	
init:
	sudo pip install -r requirements.txt