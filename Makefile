install:
	pip3 install -r requirements-travis.txt
test:
	python3 manage.py test todo
