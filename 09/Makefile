target: run test

venv/bin/activate:
	python -m venv venv

run: venv/bin/activate
	./venv/Scripts/python setup.py build
	./venv/Scripts/python setup.py install

test:
	./venv/Scripts/python tests.py

clean:
	rm -rf __pycache__
	rm -rf venv