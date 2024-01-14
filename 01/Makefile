target: run estimate test

venv/bin/activate: requirements.txt
	python -m venv venv
	./venv/Scripts/pip install -r requirements.txt

run: venv/bin/activate
	./venv/Scripts/python TicTac.py

estimate:
	./venv/Scripts/pylint TicTac.py

test:
	./venv/Scripts/python -m unittest TestTicTacGame.py

clean:
	rm -rf __pycache__
	rm -rf venv