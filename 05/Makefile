target: run test coverage lint

venv/bin/activate: requirements.txt
	python -m venv venv
	./venv/Scripts/pip install -r requirements.txt

run: venv/bin/activate

lint:
	./venv/Scripts/pylint lru_cache.py
test:
	./venv/Scripts/python -m unittest lru_cache_test.py

coverage:
	./venv/Scripts/python -m coverage run -m unittest lru_cache_test.py
	./venv/Scripts/python -m coverage report


clean:
	rm -rf __pycache__
	rm -rf venv