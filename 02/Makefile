target: run coverage lint

venv/bin/activate: requirements.txt
	python -m venv venv
	./venv/Scripts/pip install -r requirements.txt

run: venv/bin/activate
	./venv/Scripts/python json_parser.py
	./venv/Scripts/python decorator.py

lint:
	./venv/Scripts/pylint json_parser.py decorator.py

coverage:
	./venv/Scripts/coverage run -m unittest decorator_test.py
	./venv/Scripts/coverage report

clean:
	rm -rf __pycache__
	rm -rf venv