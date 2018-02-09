clean:
	find . -name *.pyc -delete

compile: clean
	python -m compileall .

release: clean
	python setup.py sdist upload


