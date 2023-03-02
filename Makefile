start:
	python3 manage.py runserver 0.0.0.0:8080

test:
	python3 manage.py test tests/

console:
	python3 manage.py shell_plus --ipython
