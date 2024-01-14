target: run test coverage lint

venv/bin/activate: requirements.txt
	python -m venv venv
	./venv/Scripts/pip install -r requirements.txt

run: venv/bin/activate
	./venv/Scripts/python customlist.py

test:
	./venv/Scripts/python -m unittest customlisttest.py

lint:
	./venv/Scripts/pylint customlist.py

coverage:
	./venv/Scripts/python -m coverage run -m unittest customlist.py
	./venv/Scripts/python -m coverage report

clean:
	rm -rf __pycache__
	rm -rf venv