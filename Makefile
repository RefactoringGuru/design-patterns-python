codestyle-check:
	find . -name \*.py -exec pycodestyle --max-line-length=200 --ignore=W293 --count {} +
	
init:
	sudo pip install -r requirements.txt